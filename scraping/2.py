#!/usr/bin/python
# encoding:utf-8

import requests
from bs4 import BeautifulSoup

html_sample = '''
<html>
    <body>
    <h1 id='title'>Hello world</h1>
    <a href="#" class="link">This is link1</a>
    <a href="# link2" class="link">This is link2</a>
    </body>
</html>'''

soup = BeautifulSoup(html_sample, 'html.parser')
# print(soup.text)
# header = soup.select('h1')
# print(header)
# print(header[0].text)

# header = soup.select('a')
# for link in header:
#     print(link.text)

# 使用select找出所有id为title的元素（id前面需加#）
# alink = soup.select('#title')
# print(alink)

# 使用select找出所有class为link的元素（class前面需加.）
# for link in soup.select('.link'):
#     print(link)

# for link in soup.select('a'):
#     print(link)
#     print(link['href'])

# a = '<a href="#" qoo=123 abc=456>I am a link</a>'
# soup=BeautifulSoup(a, 'html.parser')
# print(soup.select('a'))
# print(soup.select('a')[0])
# print(soup.select('a')[0]['abc'])