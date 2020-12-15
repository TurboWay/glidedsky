#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/7 13:18
# @Author : way
# @Site : 
# @Describe: 爬虫-字体反爬-2

import base64
from fontTools.ttLib import TTFont

import re
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from tempfile import TemporaryFile
from env import headers


def crawler(url):
    text = requests.get(url, headers=headers).text
    font_face = re.findall('base64,(.*?)\)', text)
    with TemporaryFile() as f:
        f.write(base64.b64decode(font_face[0]))
        f.seek(0)
        font = TTFont(f)
    # font.saveXML('glided_sky.xml')  # 转换成xml
    number_list = font.getGlyphOrder()[1:11]
    font_map = font.getBestCmap()
    rows = BeautifulSoup(text, 'lxml').find_all('div', class_="col-md-1")
    scores = []
    for row in rows:
        numbers = []
        for font in row.text.strip():
            unicode_str = font.encode('unicode-escape').decode()
            sixteen_str = unicode_str.replace('\\u', '0x')
            # print(int(sixteen_str, 16))
            number = number_list.index(font_map[int(sixteen_str, 16)])
            numbers.append(str(number))
        scores.append(int(''.join(numbers)))
    print(f"第{url.split('=')[-1]}页 合计:{sum(scores)} 明细:{scores}")
    return sum(scores)


if __name__ == "__main__":
    urls = []
    for i in range(1, 1001):
        url = f'http://www.glidedsky.com/level/web/crawler-font-puzzle-2?page={i}'
        urls.append(url)
    pool = ThreadPoolExecutor(max_workers=10)
    score = 0
    for result in pool.map(crawler, urls):
        score += result
    print(score)  # 2657363
