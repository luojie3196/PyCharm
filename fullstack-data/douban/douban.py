#!/usr/bin/python
# encoding:utf-8

import requests
import json
from bs4 import BeautifulSoup
import re
import pymysql


def insert_info(movie_dict):
    conn = pymysql.connect(host="localhost", user="root", password="93560",
                           db="db_int", port=3306, charset="utf8")
    cur = conn.cursor()
    query = 'select movie_id from douban'
    cur.execute(query)
    fetchall = cur.fetchall()
    all_id = []
    for num in fetchall:
        all_id.append(num[0])
    if int(movie_dict["movie_id"]) not in all_id:
        query = 'insert into douban(title, movie_id, rate, url, director, \
            scriptwriter, protagonist, type, region, language, release_time, \
            run_time, other_title, imdb_link, website, comment_num, summary)\
            values("%s", "%s", "%s", "%s", "%s", "%s", "%s", \
            "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' \
              % (movie_dict["title"], movie_dict["movie_id"],
                 movie_dict["rate"], movie_dict["url"],
                 movie_dict["director"], movie_dict["scriptwriter"],
                 movie_dict["protagonist"], movie_dict["type"],
                 movie_dict["region"], movie_dict["language"],
                 movie_dict["release_time"], movie_dict["run_time"],
                 movie_dict["other_title"], movie_dict["imdb_link"],
                 movie_dict["website"], movie_dict["comment_num"],
                 movie_dict["summary"])

        print("query:", query)
        cur.execute(query)
    cur.close()
    conn.close()

# insert_info()
# exit(0)

url = "https://movie.douban.com/j/search_tags?type=movie"
res = requests.get(url)
tag_dict = json.loads(res.text)
tags = tag_dict["tags"]
# tags = tags[:1]
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
print(movie_list)
# key_list = []
# val_list = []
movie_dict = {}
movies_list = []
for movie in movie_list:
    # print(movie)
    url = movie["url"]
    movie_dict["movie_id"] = movie["id"]
    movie_dict["url"] = url
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
    info_dict = {
        "导演": "director",
        "编剧": "scriptwriter",
        "主演": "protagonist",
        "类型": "type",
        "制片国家/地区": "region",
        "语言": "language",
        "上映日期": "release_time",
        "片长": "run_time",
        "又名": "other_title",
        "IMDb链接": "imdb_link",
        "官方网站": "website",
        "官方小站": "website"
    }
    movie_dict["website"] = ''
    for line in info_text.split("\n"):
        new_line = line.split(":")
        if len(new_line) > 1:
            print(new_line)
            movie_dict[info_dict[new_line[0]]] = new_line[1]
    # break
    # movie_dict["info"] = info_text
    related_text = soup.select(".related-info #link-report")[0].text
    # print("related text: ", related_text)
    # summary = related_text.replace(" ", "").replace("\n", "").strip("©豆瓣").replace("\u3000\u3000", "")  # .split("\n")[-1].strip()
    summary = ''
    tmp_summary = related_text.strip().split("\n")  # .split("\n")[-1].strip()
    for line in tmp_summary:
        if len(line) == 0:
            continue
        summary += line.strip().strip("©豆瓣")
    movie_dict["summary"] = summary
    # print(info_text)
    # print(related_text)
    # 获取评论数
    comment_num = soup.select('.mod-hd h2 .pl a')
    comment_num = re.sub(r"\D+", "", comment_num[0].text)
    movie_dict['comment_num'] = comment_num
    print(movie_dict)
    insert_info(movie_dict)
    # for key in movie_dict:
    #     print(key)
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

# fw = open("movies.json", "w", encoding="utf-8")
# fw.write(json.dumps(movies_list))
# fw.close()

