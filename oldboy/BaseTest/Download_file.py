#!/usr/bin/python
# encoding:utf-8

import urllib
import os
import time

url = 'http://codown.youdao.com/cidian/download/YoudaoDictBeta.exe'
name = os.path.basename(url)

def report_hook(count, block_size, total_size):
    print ('%d%%'%(100.0 * count * block_size/ total_size))
    time.sleep(2)

urllib.urlretrieve(url, name, reporthook= report_hook)