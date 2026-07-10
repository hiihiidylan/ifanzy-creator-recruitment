#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate complete 17-page creator recruitment HTML files"""

def read_source_html():
    """Read the source HTML to extract CSS and JS"""
    with open('/Users/kwok/Desktop/ifanzy宣传物料/机构合作/agency_partnership_v4_tc.html', 'r', encoding='utf-8') as f:
        return f.read()

def generate_html(lang='en'):
    """Generate complete HTML for English or Traditional Chinese"""

    source = read_source_html()

    # Extract styles (everything between <style> and </style>)
    style_start = source.find('<style>')
    style_end = source.find('</style>') + len('</style>')
    styles = source[style_start:style_end]

    # Extract script (everything between <script> and </script>)
    script_start = source.find('<script>')
    script_end = source.find('</script>') + len('</script>')
    script = source[script_start:script_end]

    if lang == 'en':
        return generate_en_html(styles, script)
    else:
        return generate_tc_html(styles, script)

def generate_en_html(styles, script):
    """Generate English version"""
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>iFanzy Creator Recruitment - Your AI Twin Works While You Sleep</title>
{styles}
</head>
<body>

<div class="wordmark">iFanzy</div>

<div class="lang-switcher">
<a href="creator_recruitment.html" class="lang-btn active">EN</a>
<a href="creator_recruitment_tc.html" class="lang-btn">繁中</a>
</div>

<!-- Slide 1: Hero -->
<section class="slide">
<div class="content center">
<div class="kicker">Creator Recruitment</div>
<h1>Your AI Twin<br/>Works While You Sleep</h1>
<p class="tagline">
Clone yourself with AI. Earn 24/7. Keep full control.
</p>
<div class="accent"></div>
<div style="margin-top:clamp(48px,6vh,64px)">
<a href="#contact" class="btn">Join Now →</a>
</div>
</div>
</section>

<!-- Slide 2: 24-Hour Challenge -->
