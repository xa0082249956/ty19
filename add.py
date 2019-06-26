#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import re

reals='''中国政法大学
欢迎加入2019法大铁一宣讲答疑群，群聊号码：741015561点击链接加入群聊【2019法大铁一宣讲答疑群】：https://jq.qq.com/?_wv=1027&k=5IZhdf6
成都所有大学
欢迎加入2018成都铁一群，群聊号码：831209410点击链接加入群聊【2018成都铁一群】：https://jq.qq.com/?_wv=1027&k=5cQYYbv
南开大学
欢迎加入南开大学新生咨询群，群聊号码：565054623点击链接加入群聊【南开大学新生咨询群】：https://jq.qq.com/?_wv=1027&k=54f2OHe
四川大学
欢迎加入四川大学，群聊号码：730545368点击链接加入群聊【四川大学】：https://jq.qq.com/?_wv=1027&k=5TWK8SX
'''

def extract(univ, s):
    num = re.findall(r'群聊号码：(\d+)', s)[0]
    name, link = re.findall(r'点击链接加入群聊【(.+?)】：([0-9a-zA-Z\?/:_=\.\&]+)', s)[0]

    print(f'|{univ}|[{num}]({link})|{name}|')

reals = reals.split('\n')
for i in range(len(reals)//2):
    extract(reals[i*2], reals[i*2+1])
