#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import urllib.request
import time
import sys


# reporthook(blocknum, bs, size)
def reporthook(blocknum, bs, size):
    '''''
    blocknum:已经下载的数据块
    bs:数据块的大小
    size:远程文件的大小
   '''
    per = 100.0 * blocknum * bs / size
    if per > 100 :
        per = 100
    # print('%.2f%%' % per)
    # sys.stdout.reset()
    sys.stdout.write('%.2f%%\n' % per)
    sys.stdout.flush()
    time.sleep(5)

def download_file(url):
    file_name = os.path.basename(url)
    print(os.getcwd() + r'\python_vedio\\' + file_name)
    file_name = os.getcwd() + r'\python_vedio\\' + file_name
    res = urllib.request.urlretrieve(url, file_name, reporthook)


# url = 'https://repo.continuum.io/archive/Anaconda3-4.2.0-Windows-x86_64.exe'
# url = 'http://video.ch9.ms/ch9/3269/3dc632f2-8a7c-43e2-a4ff-4821bb1a3269/IntrotoPythonM01_high.mp4'
# download_file(url)

# 'http://video.ch9.ms/ch9/3269/3dc632f2-8a7c-43e2-a4ff-4821bb1a3269/IntrotoPythonM01_high.mp4',
# 'http://video.ch9.ms/ch9/7acc/1252bed1-4210-4a22-bfa7-ec44f5be7acc/IntrotoPythonM02_high.mp4',
# 'http://video.ch9.ms/ch9/1ba2/d3a04d41-3a21-4c32-b7bc-bfd6d1c41ba2/IntrotoPythonM03_high.mp4',
# 'http://video.ch9.ms/ch9/e14c/2073ad6d-7b90-468b-9687-e4d64d22e14c/IntrotoPythonM04_high.mp4',
# 'http://video.ch9.ms/ch9/222b/6e41a575-af23-4131-92d1-27789861222b/IntrotoPythonM05_high.mp4',
# 'http://video.ch9.ms/ch9/6bee/ad031b8f-e3d3-468e-91c5-870a51826bee/IntrotoPythonM06_high.mp4',
# 'http://video.ch9.ms/ch9/508c/52855873-1ee8-4c68-86cd-ce1ab0a2508c/IntrotoPythonM07_high.mp4',
# 'http://video.ch9.ms/ch9/0076/91c85004-3d37-4033-b3ea-623edc970076/IntrotoPythonM08_high.mp4',
# 'http://video.ch9.ms/ch9/0b6b/fb5058a4-3f48-4fe0-86d5-242489060b6b/IntrotoPythonM09_high.mp4',
# 'http://video.ch9.ms/ch9/d19f/8fc3b502-b03f-4d13-a34f-053dc368d19f/IntrotoPythonM10_high.mp4',
# 'http://video.ch9.ms/ch9/40f9/33b0d5ea-e056-4dbe-9957-39f751c040f9/IntrotoPythonM11_high.mp4',
# 'http://video.ch9.ms/ch9/4acb/2ff70f4d-bdd0-4dec-bf13-3301278c4acb/IntrotoPythonM12_high.mp4',

url_list = [
'http://video.ch9.ms/ch9/51a2/a73efeea-710a-400f-9792-588cddee51a2/IntrotoPythonM13_high.mp4',
'http://video.ch9.ms/ch9/17c6/ba85d26f-e285-4fa6-a496-f35a9e2d17c6/IntrotoPythonM14_high.mp4'
]


for url in url_list:
    # print(url)
    download_file(url)