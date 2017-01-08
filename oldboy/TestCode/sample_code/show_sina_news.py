#!/usr/bin/python
# encoding:utf-8

import pymysql

def show_sina_news():
    conn = pymysql.connect(host = 'localhost', user = 'root', password = '93560', db = 'db_int', port = 3306, charset="utf8")
    cur = conn.cursor()
    query = "select DISTINCT id, title, time, article, editor, media_name from sina_news"
    print(query)
    cur.execute(query)
    news = cur.fetchall()
    cur.close()
    conn.close()
    return news

num = 0
news = show_sina_news()
for line in news:
    num += 1
    print(line)
print(num)