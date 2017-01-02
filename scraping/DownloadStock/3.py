#!/usr/bin/python
# encoding:utf-8

# python 2.7
import urllib

goog_url = 'http://chart.finance.yahoo.com/table.csv?s=GOOG&a=11&b=4&c=2005&d=11&e=4&f=2016&g=d&ignore=.csv'

def get_html(url):
    url_open = urllib.urlopen(url)
    text = url_open.read().split('\n')
    return text

def get_stock_data(text):
    fx = open(r'goog.csv', 'w')
    for line in text:
        fx.write(line + '\n')
    fx.close()

html = get_html(goog_url)
get_stock_data(html)
