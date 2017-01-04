#!/usr/bin/python
# encoding:utf-8

import requests
import json

url = "https://movie.douban.com/j/search_tags?type=movie"
res = requests.get(url)
tag_dict = json.loads(res.text)
tags = tag_dict["tags"]

fw = open("movies.csv", "w", encoding="utf-8")
for tag in tags:
    page = 0
    while True:
        url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%s&sort=recommend&page_limit=20&page_start=%s" \
              % (tag, page)
        print(url)
        res = requests.get(url)
        movies = json.loads(res.text)["subjects"]
        if not movies:
            break
        for movie in movies:
            title = movie["title"]
            link = movie["url"]
            rate = movie["rate"]
            id = movie["id"]
            fw.write("%s,%s,%s,%s,%s\n" % (tag, id, title, link, rate))
        page += 20
fw.close()
