#!/usr/bin/python
# encoding:utf-8

import urllib


def report_hook(count, block_size, total_size):
    print('%02d%%'%(100.0 * count * block_size/ total_size))

url = "http://cdn.mysql.com//Downloads/MySQLInstaller/mysql-installer-community-5.7.16.0.msi"
urllib.urlretrieve(url, 'mysql-installer-community-5.7.16.0.msi', reporthook= report_hook)
