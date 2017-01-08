#!/usr/bin/python
# -*- coding:utf-8 -*-

import re
# import urllib
import urllib.request


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getRemotePath(html):
    reg = r'project name="(.*?)"'
    rReg = re.compile(reg)
    pathList = re.findall(rReg, html)
    return pathList

def getLocalPath(html):
    reg = r'" path="(.*?)"'
    rReg = re.compile(reg)
    pathList = re.findall(rReg, html)
    return pathList


html = getHtml("http://172.16.11.162/gitweb-fast/gitweb-winphone/?p=manifests.git;a=blob_plain;f=w8996.xml;hb=master")
remoteList = getRemotePath(html)
localList = getLocalPath(html)

print(zip(remoteList, localList))
