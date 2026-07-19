const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');
const { PDFDocument } = require('pdf-lib');

const chromePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const outputDir = path.join(__dirname, 'outputs', 'pdf');
const previewOptions = {
  // Match the current in-app preview viewport exactly. The deck uses vw/vh
  // extensively, so a different outer viewport produces a different layout
  // even when the cropped slide itself is still 4:3.
  viewportWidth: 1155,
  viewportHeight: 819,
  slideWidth: 1092,
  slideHeight: 819,
  pdfWidth: 1600,
  pdfHeight: 1200,
  deviceScaleFactor: 2,
};

async function generatePDF(htmlFile, outputPdf) {
  console.log(`Generating ${outputPdf}...`);

  const browser = await puppeteer.launch({
    executablePath: chromePath,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage'],
  });

  try {
    const page = await browser.newPage();
    await page.setViewport({
      width: previewOptions.viewportWidth,
      height: previewOptions.viewportHeight,
      deviceScaleFactor: previewOptions.deviceScaleFactor,
    });

    const htmlPath = path.join(__dirname, htmlFile);
    await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0' });

    await page.evaluate(() => {
      // The desktop preview reserves a 15px vertical scrollbar gutter. Headless
      // Chrome uses overlay scrollbars, so reproduce that same centering width.
      document.body.style.width = 'calc(100% - 15px)';
      const langSwitch = document.querySelector('.lang-switcher');
      if (langSwitch) {
        langSwitch.style.display = 'none';
      }
    });

    await page.evaluate(async () => {
      await document.fonts.ready;
      await new Promise((resolve) => requestAnimationFrame(() => requestAnimationFrame(resolve)));
    });
    await new Promise((resolve) => setTimeout(resolve, 500));

    const slideCount = await page.evaluate(() => document.querySelectorAll('.slide').length);
    console.log(`Found ${slideCount} slides`);

    const screenshots = [];

    for (let index = 0; index < slideCount; index += 1) {
      await page.evaluate((slideIndex) => {
        const slides = document.querySelectorAll('.slide');
        slides.forEach((slide) => {
          slide.style.scrollSnapAlign = 'none';
        });
        window.scrollTo({
          top: slides[slideIndex].offsetTop,
          left: 0,
          behavior: 'instant',
        });
      }, index);

      await new Promise((resolve) => setTimeout(resolve, 250));

      const slideFrame = await page.evaluate((slideIndex) => {
        const rect = document.querySelectorAll('.slide')[slideIndex].getBoundingClientRect();
        return {
          left: rect.left,
          top: rect.top,
          width: rect.width,
          height: rect.height,
          viewportWidth: window.innerWidth,
          viewportHeight: window.innerHeight,
          scrollX: window.scrollX,
          scrollY: window.scrollY,
        };
      }, index);

      const frameMatchesPreview =
        Math.abs(slideFrame.top) < 0.5 &&
        Math.abs(slideFrame.width - previewOptions.slideWidth) < 0.5 &&
        Math.abs(slideFrame.height - previewOptions.slideHeight) < 0.5 &&
        Math.abs(slideFrame.viewportWidth - previewOptions.viewportWidth) < 0.5 &&
        Math.abs(slideFrame.viewportHeight - previewOptions.viewportHeight) < 0.5;

      if (!frameMatchesPreview) {
        throw new Error(
          `Slide ${index + 1} does not match the browser preview frame: ${JSON.stringify(slideFrame)}`,
        );
      }

      const screenshot = await page.screenshot({
        type: 'png',
        clip: {
          // Match the visible preview capture, which includes its narrow left
          // canvas gutter instead of beginning at the slide's DOM boundary.
          x: slideFrame.scrollX,
          y: slideFrame.scrollY + slideFrame.top,
          width: slideFrame.width,
          height: slideFrame.height,
        },
      });
      screenshots.push(screenshot);
      console.log(`Captured slide ${index + 1}/${slideCount}`);
    }

    fs.mkdirSync(outputDir, { recursive: true });
    const pdfDoc = await PDFDocument.create();

    for (const screenshot of screenshots) {
      const image = await pdfDoc.embedPng(screenshot);
      const pdfPage = pdfDoc.addPage([previewOptions.pdfWidth, previewOptions.pdfHeight]);
      pdfPage.drawImage(image, {
        x: 0,
        y: 0,
        width: previewOptions.pdfWidth,
        height: previewOptions.pdfHeight,
      });
    }

    const outputPath = path.join(outputDir, outputPdf);
    fs.writeFileSync(outputPath, await pdfDoc.save());
    console.log(`PDF generated: ${outputPath}`);
    return outputPath;
  } finally {
    await browser.close();
  }
}

(async () => {
  try {
    await generatePDF('creator_recruitment_4x3.html', 'creator_recruitment_4x3_en.pdf');
    await generatePDF('creator_recruitment_tc_4x3.html', 'creator_recruitment_4x3_tc.pdf');
    console.log('All 4:3 PDFs generated successfully.');
  } catch (error) {
    console.error(error);
    process.exit(1);
  }
})();
