#!/usr/bin/python
# encoding:utf-8

import requests
from bs4 import BeautifulSoup

res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'
# print(type(res))
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
# print(type(soup))
print(soup.text)