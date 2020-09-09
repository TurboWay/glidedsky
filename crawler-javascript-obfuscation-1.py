#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/8 14:47
# @Author : way
# @Site : 
# @Describe: 爬虫-JS加密1

import time
import hashlib
import requests
from concurrent.futures import ThreadPoolExecutor
from env import headers


def crawler(url):
    t = int(time.time())
    sign = hashlib.sha1(f'Xr0Z-javascript-obfuscation-1{t}'.encode('utf-8')).hexdigest()
    url = url + f'&t={t}&sign={sign}'
    response = requests.get(url, headers=headers).json()
    rows = response.get('items')
    score = sum(rows)
    return score


if __name__ == "__main__":
    urls = []
    for i in range(1, 1000 + 1):
        url = f'http://www.glidedsky.com/api/level/web/crawler-javascript-obfuscation-1/items?page={i}'
        urls.append(url)
    pool = ThreadPoolExecutor(max_workers=10)
    score = 0
    for result in pool.map(crawler, urls):
        score += result
    print(score)  # 2907074
