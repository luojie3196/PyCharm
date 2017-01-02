#!/usr/bin/python
# encoding:utf-8

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json

all_result = []


def main(link):
    res = requests.get(link)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    news = soup.select('.news-item')
    for new in news:
        result = {}
        if len(new.select('h2')) > 0:
            # h2 = new.select('h2')[0].text
            # time = new.select('.time')[0].text
            link = new.select('a')[0]['href']
            # print(time, h2, link)
            title, time, media_name, article, editor = get_context(link)
            result['title'] = title
            result['time'] = time
            result['media_name'] = media_name
            result['article'] = article
            result['editor'] = editor
            result['comment'] = get_comment_counts(link)
            all_result.append(result)
    return all_result


def get_context(link):
    res = requests.get(link)
    res.encoding = 'uft-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.select('#artibodyTitle')
    title = title[0].text

    # comment = soup.select('#commentCount1')
    # print(comment)
    time_source = soup.select('.time-source')[0].contents[0].strip()
    time = datetime.strptime(time_source, '%Y年%m月%d日%H:%M')
    # media_name = soup.select('.time-source')[0].contents[1].text
    media_name = soup.select('.time-source span a')[0].text

    article = []
    news = soup.select('#artibody p')[:-1]
    for new in news:
        article.append(new.text.strip())
    article = ' '.join(article)
    editor = soup.select('.article-editor')
    editor = editor[0].text.strip('责任编辑：')
    return title, time, media_name, article, editor


def get_comment_counts(link):
    news_id = re.findall(r'/doc-i(.*?).shtml', link)
    comment_url = 'http://comment5.news.sina.com.cn/page/info?\
    version=1&format=js&channel=gn&newsid=comos-{}&\
    group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
    comments = requests.get(comment_url.format(news_id[0]))
    jd = json.loads(comments.text.strip('var data='))
    total_counts = jd['result']['count']['total']
    return total_counts

all_result = main('http://news.sina.com.cn/china/')
num = 0
for news in all_result:
    num += 1
    for k, v in news.items():
        print(k, v)
    print('*' * 40)
print(num)
# get_context('http://news.sina.com.cn/c/nd/2016-12-11/doc-ifxypipu7688816.shtml')
# get_context(link)