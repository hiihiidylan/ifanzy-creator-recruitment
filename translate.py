#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# 读取英文版
with open('creator_recruitment.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 完整翻译映射
translations = [
    ('lang="en"', 'lang="zh-TW"'),
    ('iFanzy Creator Program - Your AI Twin Works While You Sleep', 'iFanzy 創作者計劃 - 你的AI分身在你睡覺時工作'),
    ('creator_recruitment.html" class="lang-btn active">EN', 'creator_recruitment.html" class="lang-btn">EN'),
    ('creator_recruitment_tc.html" class="lang-btn">繁中', 'creator_recruitment_tc.html" class="lang-btn active">繁中'),

    # Page 1
    ('BECOME AN AI CREATOR', '成為AI創作者'),
    ('Your AI Twin Works<br/>While You Sleep', '你的AI分身<br/>在你睡覺時工作'),
    ('Turn yourself into a 24/7 AI creator with iFanzy.<br/>Clone yourself. Work less. Earn more.', '用iFanzy把自己變成全天候AI創作者。<br/>複製自己。少做多賺。'),
    ('Create My AI Twin Now →', '立即創建我的AI分身 →'),

    # Page 2
    ("THE CREATOR'S REALITY", '創作者的現實'),
    ("You're Always Working.<br/>But Never <span class=\"yellow\">Enough</span>", '你總是在工作。<br/>但永遠<span class="yellow">不夠</span>'),
    ('No time to rest. Revenue stops when you stop.', '沒有休息時間。當你停下來，收入也停止了。'),
    ('<div class="time">6AM</div>', '<div class="time">早上6點</div>'),
    ('<div class="task">📸<br/>Shoot Content</div>', '<div class="task">📸<br/>拍攝內容</div>'),
    ('<div class="time">10AM</div>', '<div class="time">早上10點</div>'),
    ('<div class="task">💬<br/>Reply DMs</div>', '<div class="task">💬<br/>回覆私訊</div>'),
    ('<div class="time">2PM</div>', '<div class="time">下午2點</div>'),
    ('<div class="task">✂️<br/>Edit Videos</div>', '<div class="task">✂️<br/>剪輯影片</div>'),
    ('<div class="time">6PM</div>', '<div class="time">下午6點</div>'),
    ('<div class="task">📱<br/>Post Content</div>', '<div class="task">📱<br/>發布貼文</div>'),
    ('<div class="time">10PM</div>', '<div class="time">晚上10點</div>'),
    ('<div class="task">🎥<br/>Go Live</div>', '<div class="task">🎥<br/>直播</div>'),
    ('<div class="time">2AM</div>', '<div class="time">凌晨2點</div>'),
    ('<div class="task">👥<br/>Manage Fans</div>', '<div class="task">👥<br/>管理粉絲</div>'),
    ('<div class="time" style="font-size:clamp(16px,1.8vw,22px)">4AM</div>', '<div class="time" style="font-size:clamp(16px,1.8vw,22px)">凌晨4點</div>'),
    ('<div class="task" style="color:var(--yellow);font-weight:700">😴<br/>Still Replying...</div>', '<div class="task" style="color:var(--yellow);font-weight:700">😴<br/>還在回覆...</div>'),

    # Page 3
    ('THE BOTTLENECK', '瓶頸所在'),
    ('<span class="yellow">24</span> Hours. <span class="yellow">24</span> Time Zones.<br/><span class="yellow">∞</span> Fans Waiting', '<span class="yellow">24</span> 小時。<span class="yellow">24</span> 個時區。<br/><span class="yellow">∞</span> 粉絲在等待'),
    ('<h3>67%</h3>\n<p>Fans online when you sleep</p>', '<h3>67%</h3>\n<p>粉絲在你睡覺時在線</p>'),
    ('<h3>83%</h3>\n<p>DMs go unanswered</p>', '<h3>83%</h3>\n<p>私訊未被回覆</p>'),
    ('<h3>100%</h3>\n<p>Revenue stops when you rest</p>', '<h3>100%</h3>\n<p>休息時收入停止</p>'),
    ('Your time is limited. Your potential is not.', '你的時間有限。你的潛力無限。'),
]

# 执行替换
for en, zh in translations:
    html = html.replace(en, zh)

# 保存
with open('creator_recruitment_tc.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Translation completed!")
