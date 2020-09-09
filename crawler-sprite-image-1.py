#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/8 15:21
# @Author : way
# @Site : 
# @Describe: 爬虫-雪碧图-1

import base64
import re
from PIL import Image
from io import BytesIO

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from env import headers


def img_split(pixels, width, height):
    """
    :param pixels: pixels[x,y] 只有两个值 0表示黑，255表示白
    :param width: 图片宽度 x
    :param height: 图片高度 y
    :return: 对 x 轴上的，每一个 y 列的像素点做颜色判断，获取一个如下的 x 轴白色点位的列表，相邻的两个点位之间即为 黑色的数字
    [0, 11, 25, 40, 52, 66, 80, 95, 107, 118, 131]
    """
    def get_black_start(white_start):
        for x in range(white_start, width):
            for y in range(height):
                if pixels[x, y] == 0:
                    return x

    def get_white_start(black_start):
        for x in range(black_start, width):
            for y in range(height):
                if pixels[x, y] == 0:
                    break
            else:
                return x

    white_start = 0
    position_list = [white_start]
    for _ in range(10):
        black_start = get_black_start(white_start)
        white_start = get_white_start(black_start)
        position_list.append(white_start)
    return position_list


def get_position_list(text):
    """
    :param text: 将图片转化为 二值图像，非黑即白
    :return:
    """
    img_str = re.findall('base64,(.*?)\)', text)[0]
    img_fp = BytesIO(base64.b64decode(img_str.encode('utf-8')))
    img = Image.open(img_fp).convert('1')
    # img.show()
    pixels = img.load()
    position_list = img_split(pixels, img.width, img.height)
    return position_list


def crawler(url):
    text = requests.get(url, headers=headers).text
    position_list = get_position_list(text)
    rows = BeautifulSoup(text, 'lxml').find_all('div', class_="col-md-1")
    scores = []
    for row in rows:
        nums = []
        for div in row.find_all('div'):
            css_name = div.get('class')[0].split(' ')[0]
            tag_x = re.findall(f'\.{css_name} \{{ background-position-x:(.*?)px \}}', text)
            tag_x = abs(int(tag_x[0]))
            for idx, x in enumerate(position_list):
                if x <= tag_x <= position_list[idx + 1]:
                    nums.append(str(idx))
                    break
        scores.append(int(''.join(nums)))
    print(f"第{url.split('=')[-1]}页 合计:{sum(scores)} 明细:{scores}")
    return sum(scores)


if __name__ == "__main__":
    urls = []
    for i in range(1, 1001):
        url = f'http://www.glidedsky.com/level/web/crawler-sprite-image-1?page={i}'
        urls.append(url)

    pool = ThreadPoolExecutor(max_workers=20)
    score = 0
    for result in pool.map(crawler, urls):
        score += result
    print(score)  # 2901718
