#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 读取模板文件
with open('/Users/kwok/Desktop/ifanzy宣传物料/机构合作/agency_partnership_v4_tc.html', 'r', encoding='utf-8') as f:
    template = f.read()

# 提取CSS部分
css_start = template.find('<style>')
css_end = template.find('</style>') + 8
css_section = template[css_start:css_end]

# 提取JavaScript部分
js_start = template.find('<script>')
js_end = template.find('</script>') + 9
js_section = template[js_start:js_end]

# 英文版HTML头部
html_en_head = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>iFanzy Creator Recruitment - Your AI Twin Works While You Sleep</title>
{css_section}
</head>
<body>

<div class="wordmark">iFanzy</div>

<div class="lang-switcher">
<a href="creator_recruitment.html" class="lang-btn active">EN</a>
<a href="creator_recruitment_tc.html" class="lang-btn">繁中</a>
</div>
'''

# 繁中版HTML头部
html_tc_head = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>iFanzy 創作者招募 - 你的AI分身在你睡覺時工作</title>
{css_section}
</head>
<body>

<div class="wordmark">iFanzy</div>

<div class="lang-switcher">
<a href="creator_recruitment.html" class="lang-btn">EN</a>
<a href="creator_recruitment_tc.html" class="lang-btn active">繁中</a>
</div>
'''

# 17个section的内容 - 英文版
sections_en = '''
<!-- Slide 1: Hero -->
<section class="slide">
<div class="content center">
<div class="kicker">AI CREATOR REVOLUTION</div>
<h1>Your AI Twin Works<br/>While You Sleep</h1>
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
<section class="slide">
<div class="content center">
<div class="kicker">THE CREATOR'S DILEMMA</div>
<h2>You Only Have<br/><span class="yellow">24 Hours</span></h2>
<div class="flow">
<div class="step">
<div class="num">6 AM</div>
<h3>Content Creation</h3>
<p>Shooting & editing</p>
</div>
<div class="step">
<div class="num">12 PM</div>
<h3>Fan Replies</h3>
<p>DMs & comments</p>
</div>
<div class="step">
<div class="num">6 PM</div>
<h3>Live Stream</h3>
<p>Engaging fans</p>
</div>
<div class="step">
<div class="num">12 AM</div>
<h3>Admin Work</h3>
<p>Planning & analytics</p>
</div>
<div class="step" style="background:linear-gradient(145deg,rgba(255,198,26,.15),rgba(255,198,26,.08));border-color:rgba(255,198,26,.5)">
<div class="num">→</div>
<h3 style="color:var(--yellow)">Burnout</h3>
<p style="color:var(--gray)">Never enough time</p>
</div>
</div>
</div>
</section>

<!-- Slide 3: The Bottleneck -->
<section class="slide">
<div class="content">
<div class="two">
<div>
<div class="kicker">THE IMPOSSIBLE EQUATION</div>
<h2>24 Hours × 24 Timezones<br/>× <span class="yellow">∞ Fans</span></h2>
<div class="list">
<div class="item"><span class="mark">→</span> Fans expect instant replies</div>
<div class="item"><span class="mark">→</span> Global audience, local hours</div>
<div class="item"><span class="mark">→</span> Can't scale personal interaction</div>
<div class="item"><span class="mark">→</span> Miss revenue while you sleep</div>
<div class="item"><span class="mark">→</span> More fans = more burnout</div>
</div>
</div>
<div style="text-align:center">
<div class="big-number">24</div>
<p style="margin-top:clamp(24px,3vh,36px);font-size:clamp(20px,2.4vw,28px);color:var(--yellow);font-weight:700;letter-spacing:-.015em">
Hours in a day.<br/>But fans want you 24/7.
</p>
</div>
</div>
</div>
</section>
'''

print("Script template created successfully")
print(f"CSS section length: {len(css_section)}")
print(f"JS section length: {len(js_section)}")
