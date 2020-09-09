#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/4 18:02
# @Author : way
# @Site :
# @Describe: 爬虫-基础1

import requests
from bs4 import BeautifulSoup
from env import headers


def crawler(url):
    response = requests.get(url, headers=headers)
    rows = BeautifulSoup(response.text, 'lxml').find_all('div', class_="col-md-1")
    score = sum(int(row.text) for row in rows)
    return score


if __name__ == "__main__":
    url = f'http://www.glidedsky.com/level/web/crawler-basic-1'
    score = crawler(url)
    print(score)  # 293298
