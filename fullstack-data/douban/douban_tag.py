#!/usr/bin/python
# encoding:utf-8

import requests
from bs4 import BeautifulSoup
import re
import pymysql
import time
from config import HOST, USER, password, db, port, charset

count = 0


def mysql_connect():
    conn = pymysql.connect(host=HOST, user=USER, password=password,
                           db=db, port=port, charset="utf8")
    cur = conn.cursor()
    return conn, cur


def mysql_close(conn, cur):
    cur.close()
    conn.close()


def get_all_movie_id():
    conn, cur = mysql_connect()
    query = 'select movie_id from douban'
    cur.execute(query)
    fetchall = cur.fetchall()
    all_id = []
    for num in fetchall:
        all_id.append(num[0])
    mysql_close(conn, cur)
    return all_id


def insert_info(movie_dict):
    conn, cur = mysql_connect()
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
    mysql_close(conn, cur)


def get_detail_info(movie_url, all_movie_id):
    movie_dict = {}
    for url in movie_url:
        movie_dict["url"] = url
        # 获取电影ID
        movie_dict["movie_id"] = re.findall(r".*/(\d*)/", url)[0]
        all_movie_id.append(1941401)
        # 判断电影ID是否已存在数据库中，若存在忽略
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
                summary += line.strip().strip("©豆瓣").replace("\\", "").replace("\"", "\\\"")
        movie_dict["summary"] = summary
        # 获取电影评论数
        comment = soup.select('.mod-hd h2 .pl a')
        if comment:
            comment_num = re.sub(r"\D+", "", comment[0].text)
        else:
            comment_num = 0
        movie_dict['comment_num'] = comment_num
        global count
        count += 1
        if len(movie_dict) < 19:
            continue
        cur_time = time.strftime("%m/%d/%Y %H:%M", time.localtime())
        print(count, cur_time, len(movie_dict), movie_dict)
        insert_info(movie_dict)


def get_movie_tags(url):
    n = 0
    while True:
        res = requests.get(url)
        if res.status_code == requests.codes.ok:
            break
        n += 1
        print("Try %s connect %s server again..." % (str(n), url))
        time.sleep(5)
    soup = BeautifulSoup(res.text, "html.parser")
    tags = soup.select(".tagCol")
    movie_tags = []
    for tag in tags[0].select("a"):
        movie_tags.append(tag.text)
    return movie_tags


def main():
    url = "https://movie.douban.com/tag/"
    # 获取电影分类所有tag
    movie_tags = get_movie_tags(url)
    print(movie_tags)
    for tag in movie_tags:
        page = 0
        all_movie_id = get_all_movie_id()
        while True:
            url = "https://movie.douban.com/tag/%s?start=%s&type=T" \
                  % (tag, page)
            print(url)
            n = 0
            while True:
                res = requests.get(url)
                if res.status_code == requests.codes.ok:
                    break
                n += 1
                print("Try %s connect server %s again..." % (str(n), url))
                time.sleep(5)
            soup = BeautifulSoup(res.text, "html.parser")
            movie_list = soup.select(".item .pl2 a")
            if not movie_list:
                break
            movie_url = []
            for li in movie_list:
                movie_url.append(li.get("href"))
            get_detail_info(movie_url, all_movie_id)
            # 每页20条电影信息
            page += 20


if __name__ == '__main__':
    main()



