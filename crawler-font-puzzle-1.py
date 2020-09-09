#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/7 13:18
# @Author : way
# @Site : 
# @Describe: 爬虫-字体反爬-1

import base64
from fontTools.ttLib import TTFont

import re
import os
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from env import headers

number_map = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def crawler(url):
    path = f"glided_sky{url.split('=')[-1]}.ttf"
    response = requests.get(url, headers=headers)
    font_face = re.findall('base64,(.*?)\)', response.text)
    with open(path, 'wb') as f:
        f.write(base64.b64decode(font_face[0]))
    font = TTFont(path)  # 打开本地的ttf文件
    # font.saveXML('glided_sky.xml')  # 转换成xml
    # print(font.getGlyphOrder()[1:])
    font_map = {str(number_map.get(value)): str(px) for px, value in enumerate(font.getGlyphOrder()[1:])}
    rows = BeautifulSoup(response.text, 'lxml').find_all('div', class_="col-md-1")
    table = str.maketrans(font_map)
    scores = []
    for row in rows:
        score = int(row.text.translate(table))
        scores.append(score)
    os.remove(path)
    print(f"第{url.split('=')[-1]}页 合计:{sum(scores)} 明细:{scores}")
    return sum(scores)


if __name__ == "__main__":
    urls = []
    for i in range(1, 1001):
        url = f'http://www.glidedsky.com/level/web/crawler-font-puzzle-1?page={i}'
        urls.append(url)
    pool = ThreadPoolExecutor(max_workers=10)
    score = 0
    for result in pool.map(crawler, urls):
        score += result
    print(score)
