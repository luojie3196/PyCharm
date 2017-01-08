#!/usr/bin/python
# encoding:utf-8

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="93560",
                       db="db_int", port=3306, charset="utf8")
cur = conn.cursor()

fr = open("douban_movie_clean.txt", "r", encoding="utf-8")
count = 0
for line in fr:
    count += 1
    print(count)
    if count == 1:
        continue
    line = line.strip().split("^")
    if not line[-3]:
        line[-3] = 0
    if not line[4]:
        line[4] = 0.0
    query = 'insert into douban_t(title, url, rate, length, description) \
              values("%s", "%s", "%s", "%s", "%s")' \
              % (line[1], line[2], line[4], line[-3], line[-1].replace("\"", "\\\""))
    print("query: ", query)
    cur.execute(query)

fr.close()
cur.close()
conn.close()



