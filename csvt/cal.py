#!/usr/bin/python
# encoding:utf-8

import re
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'img csvt="(.*\.jpg)" />'
    p = re.compile(reg)
    imgList = re.findall(p, html)
    n = 0
    for imgUrl in imgList:
        urllib.urlretrieve(imgUrl, '%s.jpg' % n)
        n += 1
    return imgList


html = getHtml("http://fashion.huanqiu.com/news/2016-11/9745625.html")
getImg(html)