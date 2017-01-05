#!/usr/bin/python
# encoding:utf-8

import requests
import json
from bs4 import BeautifulSoup
import re

url = "https://movie.douban.com/j/search_tags?type=movie"
res = requests.get(url)
tag_dict = json.loads(res.text)
tags = tag_dict["tags"]

movie_list = []
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
            movie_list.append(movie)
            fw.write("%s,%s,%s,%s,%s\n" % (tag, id, title, link, rate))
        page += 20
        # For test below code
        # break
    # For test below code
    # break
fw.close()

# key_list = []
# val_list = []
movie_dict = {}
movies_list = []
for movie in movie_list:
    url = movie["url"]
    movie_dict["rate"] = movie["rate"]
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    title = soup.select("h1 span")[0].text
    movie_dict["title"] = title
    # print(title)
    # p1 = soup.select("#info .pl")  # [0].text
    # attrs = soup.select("#info .attrs")  # [0].text
    # print(len(p1))
    # print(p1)
    # print(attrs)
    # for n in range(0, len(p1)):
    #     key_list.append(p1[n].text)
    # for n in range(0, len(attrs)):
    #     val_list.append(attrs[n].text)
    # print("key list:", key_list)
    # print("val list:", val_list)
    info_text = soup.select("#info")[0].text
    # for line in info_text.split("\n"):
    #     print(line)
    # break
    movie_dict["info"] = info_text
    related_text = soup.select(".related-info #link-report")[0].text
    # print("related text: ", related_text)
    brief_introduction = related_text.replace(" ", "")  # .split("\n")[-1].strip()
    movie_dict["brief_introduction"] = brief_introduction
    # print(info_text)
    # print(related_text)
    # 获取评论数
    comment_num = soup.select('.mod-hd h2 .pl a')
    comment_num = re.sub(r"\D+", "", comment_num[0].text)
    movie_dict['comment_num'] = comment_num
    movies_list.append(movie_dict)
    # print(movie_dict)
    # for k, v in movie_dict.items():
    #     print(k, ": ", v)
    # print("*" * 20)
    # val_list.append(comment_num)
    # print(val_list)
    '''
    # 获取类型
    type_attrs = soup.select('#info span[property="v:genre"]')
    type_str = []
    for n in range(0, len(type_attrs)):
        type_str.append(type_attrs[n].text)
    val_list.append(" / ".join(type_str))
    # 获取制片国家/地区
    pass
    # 获取语言
    pass
    # 获取上映时间
    release_time = soup.select('#info span[property="v:initialReleaseDate"]')
    val_list.append(release_time[0].text)
    # 获取片长
    release_time = soup.select('#info span[property="v:runtime"]')
    val_list.append(release_time[0].text)
    # 获取又名
    pass
    # 获取IMDb链接
    IMDb_link = soup.select('#info a[rel="nofollow"]')
    val_list.append(IMDb_link[0].get("href"))
    # 获取剧情简介
    indent = soup.select('.indent span[property="v:summary"]')
    val_list.append(indent[0].text.strip())
    '''
    # break

fw = open("movies.json", "w", encoding="utf-8")
fw.write(json.dumps(movies_list))
fw.close()

