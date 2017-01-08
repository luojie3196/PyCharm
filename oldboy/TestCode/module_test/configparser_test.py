#!/usr/bin/python
# -- coding:utf-8 -*-

import configparser
#
#
config = configparser.ConfigParser()
config.read('config.ini')
# print(config.sections())
# # for n in config:
# #     print(n)
#
# print(config['DEFAULT']['ForwardX11'])
#
# for k,v in config['DEFAULT'].items():
#     print(k, v)


# create ini config file
# import configparser
#
# config = configparser.ConfigParser()
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'}
#
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'  # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here
# config['DEFAULT']['ForwardX11'] = 'yes'
# with open('example.ini', 'w') as configfile:
#     config.write(configfile)




# ########## 读 ##########
secs = config.sections()
print(secs)
options = config.options('section1')
print(options)

item_list = config.items('section2')
print(item_list)

val = config.get('section1','k1')
print(val)
val = config.getint('section2','k1')
print(val)

# ########## 改写 ##########
# sec = config.remove_section('section1')
# config.write(open('i.cfg', "w"))

sec = config.has_section('wupeiqi')
print(sec)
sec = config.add_section('wupeiqi')
config.write(open('i.cfg', "w"))


config.set('section1','k1','222')
config.write(open('i.cfg', "w"))

# config.remove_option('section2','k1')
# config.write(open('i.cfg', "w"))