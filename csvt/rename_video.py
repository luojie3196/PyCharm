#!/usr/bin/python
# encoding:utf-8

from __future__ import print_function
import os
import json
import shutil
import sys
import chardet
import codecs

reload(sys)

sys.setdefaultencoding('utf8')

# root_dir = r'D:\Tmp\Python'
# dest_path = r'D:\Tmp\python_video_english'
root_dir = r'D:\Tmp\Python_20161203'
dest_path = r'D:\Tmp\Python_20161203_rename'


def get_file(current_dir):
    video = ''
    json = ''
    for lst in os.listdir(current_dir):
        if os.path.splitext(lst)[1] == '.mp4':
            video_file = lst
        elif os.path.splitext(lst)[1] == '.json':
            json_file = lst
    return os.path.join(current_dir, video_file), os.path.join(current_dir, json_file)


def get_video_name(json_file):
    j_file = ''
    json_str = ''
    try:
        j_file = open(json_file, 'r')
        json_str = j_file.read()
    # except IOError, msg:
    #     print('Can not open file: ' + msg)
    except Exception as err:
        print(err)
    finally:
        if j_file:
            j_file.close()
    json_dict = json.loads(json_str)
    video_name = json_dict['partTitle'].encode('utf8')
    return video_name


def rename_video(video_file, video_real_name):
    # file_path = os.path.dirname(video_file)
    print(video_file, os.path.join(dest_path, video_real_name + '.mp4'))
    shutil.copyfile(video_file, os.path.join(dest_path, video_real_name + '.mp4'))


def main():
    content = ''
    for dirlst in os.listdir(root_dir):
        full_path = os.path.join(root_dir, dirlst)
        if os.path.isdir(full_path):
            v_file, json_file = get_file(full_path)
            # get_video_name(json_file)
            video_name = str(int(dirlst) - 1) + '.' + get_video_name(json_file).replace('/', '-')
            # content = codecs.open(dest_path + r'\content.txt', 'w', encoding='utf-8')
            # content.write(video_name + '\n')
            # content.close()
            # content = codecs.open(dest_path + r'\content.txt', 'r', encoding='utf-8')
            # video_name = content.read()
            # content.close()
            content = open(dest_path + r'\content.txt', 'a')
            content.write(video_name + '\n')
            print(video_name)
            # rename_video(v_file, dirlst)
            # rename_video(v_file, video_name)
    content.close()

main()