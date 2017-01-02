#!/usr/bin/python
# encoding:utf-8

import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'<img data-cke-saved-csvt="(.*?\.jpg)" data-csvt'
    imgReg = re.compile(reg)
    imgList = re.findall(imgReg, html)
    x = 0
    for imgUrl in imgList:
        urllib.urlretrieve(imgUrl, '%s.jpg' % x)
        x += 1

html = getHtml('http://mp.weixin.qq.com/s?__biz=MjM5OTAzNzgwMA==&mid=2650448102&idx=2&sn=f4c166e548413a0b17b1ec2a9b5c2e75&scene=0#wechat_redirect')
getImg(html)