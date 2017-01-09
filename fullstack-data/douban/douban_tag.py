#!/usr/bin/python
# encoding:utf-8

import requests
from bs4 import BeautifulSoup
import re
import pymysql

count = 0


def get_all_movie_id():
    conn = pymysql.connect(host="localhost", user="root", password="93560",
                           db="db_int", port=3306, charset="utf8")
    cur = conn.cursor()
    query = 'select movie_id from douban'
    cur.execute(query)
    fetchall = cur.fetchall()
    all_id = []
    for num in fetchall:
        all_id.append(num[0])
    return all_id


def insert_info(movie_dict):
    conn = pymysql.connect(host="localhost", user="root", password="93560",
                           db="db_int", port=3306, charset="utf8")
    cur = conn.cursor()
    query = 'insert into douban(title, movie_id, rate, url, cover, director, \
        scriptwriter, protagonist, type, region, language, release_time, \
        numbers, run_time, other_title, imdb_link, website, comment_num, summary)\
        values("%s", "%s", "%s", "%s", "%s", "%s", "%s", \
        "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' \
          % (movie_dict["title"], movie_dict["movie_id"],
             movie_dict["rate"], movie_dict["url"], movie_dict["cover"],
             movie_dict["director"], movie_dict["scriptwriter"],
             movie_dict["protagonist"], movie_dict["type"],
             movie_dict["region"], movie_dict["language"],
             movie_dict["release_time"], movie_dict["numbers"],
             movie_dict["run_time"], movie_dict["other_title"],
             movie_dict["imdb_link"], movie_dict["website"],
             movie_dict["comment_num"], movie_dict["summary"])
    query = re.sub(r"\s+", " ", query)
    print("query:", query)
    cur.execute(query)
    cur.close()
    conn.close()


def get_detail_info(movie_url, all_movie_id):
    # movie_url = ["https://movie.douban.com/subject/26683290/", "https://movie.douban.com/subject/25911694/"]
    movie_dict = {}
    for url in movie_url:
        movie_dict["url"] = url
        movie_dict["movie_id"] = re.findall(r".*/(\d*)/", url)[0]
        if int(movie_dict["movie_id"]) in all_movie_id:
            print(movie_dict["movie_id"], "ID exist, skip...")
            continue
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        # 获取电影标题
        title = soup.select("h1 span")
        if not title:
            continue
        title = title[0].text
        movie_dict["title"] = title.replace("\"", "\\\"")
        # 获取电影封面图链接
        cover_soup = soup.select("#mainpic img")
        if cover_soup:
            cover = cover_soup[0].get("src")
        else:
            cover = ""
        movie_dict["cover"] = cover
        # 获取电影评分
        rate_soup = soup.select("#interest_sectl strong")
        if rate_soup:
            rate = rate_soup[0].text
            if not rate:
                rate = 0
        else:
            rate = 0
        movie_dict["rate"] = rate
        # 获取电影基本信息
        info_text = soup.select("#info")[0].text
        info_dict = {
            "导演": "director",
            "编剧": "scriptwriter",
            "主演": "protagonist",
            "类型": "type",
            "制片国家/地区": "region",
            "语言": "language",
            "上映日期": "release_time",
            "首播": "release_time",
            "集数": "numbers",
            "片长": "run_time",
            "单集片长": "run_time",
            "又名": "other_title",
            "IMDb链接": "imdb_link",
            "官方网站": "website",
            "官方小站": "website"
        }
        # 获取电影官方网站或者官方小站
        movie_dict["website"] = ""
        movie_dict["imdb_link"] = ""
        movie_dict["numbers"] = ""
        for line in info_text.split("\n"):
            new_line = line.split(":")
            if len(new_line) > 1:
                if new_line[0] in info_dict:
                    movie_dict[info_dict[new_line[0]]] = new_line[1].strip().replace("\"", "\\\"")
        # 获取电影简介
        summary = ''
        related_text = soup.select(".related-info #link-report")
        if related_text:
            related_text = related_text[0].text
            tmp_summary = related_text.strip().split("\n")
            for line in tmp_summary:
                if len(line) == 0:
                    continue
                summary += line.strip().strip("©豆瓣").replace("\"", "\\\"")
        movie_dict["summary"] = summary
        # 获取电影评论数
        comment_num = soup.select('.mod-hd h2 .pl a')
        comment_num = re.sub(r"\D+", "", comment_num[0].text)
        movie_dict['comment_num'] = comment_num
        global count
        count += 1
        if len(movie_dict) < 19:
            continue
        print(count, len(movie_dict), movie_dict)
        insert_info(movie_dict)


def get_movie_tags(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    tags = soup.select(".tagCol")
    movie_tags = []
    for tag in tags[0].select("a"):
        movie_tags.append(tag.text)
    return movie_tags

url = "https://movie.douban.com/tag/"
movie_tags = get_movie_tags(url)
# movie_tags = ["爱情"]
movie_tags.remove("爱情")
for tag in movie_tags:
    page = 0
    all_movie_id = get_all_movie_id()
    while True:
        url = "https://movie.douban.com/tag/%s?start=%s&type=T" \
              % (tag, page)
        print(url)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        movie_list = soup.select(".item .pl2 a")
        if not movie_list:
            break
        movie_url = []
        for li in movie_list:
            movie_url.append(li.get("href"))
        get_detail_info(movie_url, all_movie_id)
        page += 20
        # For test below code
        # break
    # For test below code
    # break

