#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/4 18:02
# @Author : way
# @Site : 
# @Describe: 爬虫-IP屏蔽1

import os
import json
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from env import headers, proxies


# 重试装饰器
def retry(func):
    max_retry = 10

    def run(*args, **kwargs):
        for i in range(max_retry + 1):
            url, score = func(*args, **kwargs)
            if score > 0:
                return url, score
        return func(*args, **kwargs)

    return run


@retry
def crawler(url):
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        rows = BeautifulSoup(response.text, 'lxml').find_all('div', class_="col-md-1")
        score = sum(int(row.text) for row in rows)
    except:
        score = 0
    return url, score


def main(result_path):
    if not os.path.exists(result_path):
        with open(result_path, 'w') as f:
            json.dump({}, f)

    urls = []
    for i in range(1, 1001):
        url = f'http://www.glidedsky.com/level/web/crawler-ip-block-1?page={i}'
        urls.append(url)

    with open(result_path, 'r') as f:
        dt = json.load(f)

    for key, value in dt.items():
        if value > 0:
            urls.remove(key)
            # print(key, value)

    if not urls:
        print(sum(dt.values()))
        return True
    else:
        print(f"剩余待采集页数:{len(urls)}")
        pool = ThreadPoolExecutor(max_workers=5)
        for result in pool.map(crawler, urls):
            url, score = result
            dt[url] = score

        with open(result_path, 'w') as f:
            json.dump(dt, f)


if __name__ == "__main__":
    result_path = 'crawler-ip-block-1.json'
    while True:
        if main(result_path):
            break  # 3103341
