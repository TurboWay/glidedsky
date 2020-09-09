#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/4 18:02
# @Author : way
# @Site : 
# @Describe: 爬虫-基础2

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from env import headers


def crawler(url):
    response = requests.get(url, headers=headers)
    rows = BeautifulSoup(response.text, 'lxml').find_all('div', class_="col-md-1")
    score = sum(int(row.text) for row in rows)
    return score


if __name__ == "__main__":
    urls = []
    for i in range(1, 1001):
        url = f'http://www.glidedsky.com/level/web/crawler-basic-2?page={i}'
        urls.append(url)
    pool = ThreadPoolExecutor(max_workers=20)
    score = 0
    for result in pool.map(crawler, urls):
        score += result
    print(score)  # 2537296
