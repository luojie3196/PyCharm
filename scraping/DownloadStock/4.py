#!/usr/bin/python
# encoding:utf-8

# python 3.5
from urllib import request


def download_stock_data(url):
    response = request.urlopen(url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\\n')
    fx = open(r'google.csv', 'w')
    for line in lines:
        fx.write(line + '\n')
    fx.close()

goog_url = 'http://chart.finance.yahoo.com/table.csv?s=GOOG&a=11&b=4&c=2008&d=11&e=4&f=2016&g=d&ignore=.csv'
download_stock_data(goog_url)
