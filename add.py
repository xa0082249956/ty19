#! /usr/bin/env python3
import re

univ = input("大学名称：")
s = input()
num = re.findall(r'群聊号码：(\d+)', s)[0]
name, link = re.findall(r'点击链接加入群聊【(.+?)】：([0-9a-zA-Z\?/:_=\.\&]+)', s)[0]

print(f'|{univ}|[{num}]({link})|{name}|')
