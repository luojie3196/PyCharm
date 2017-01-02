#!/usr/bin/python
# encoding:utf-8

import urllib
import os
import time

url = 'https://repo.continuum.io/archive/Anaconda3-4.2.0-Windows-x86_64.exe'
name = os.path.basename(url)

def report_hook(count, block_size, total_size):
    print ('%d%%'%(100.0 * count * block_size/ total_size))
    time.sleep(2)

urllib.urlretrieve(url, name, reporthook= report_hook)