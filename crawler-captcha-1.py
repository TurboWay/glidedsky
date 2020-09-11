#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/8 17:05
# @Author : way
# @Site :
# @Describe: 爬虫-验证码-1

import urllib3
import numpy as np
import time
import os
import cv2
import psutil
import json
import shutil

from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from random import randint

from env import cookies


def kill_process(name):
    pids = []
    all_pids = psutil.pids()

    for pid in all_pids:
        p = psutil.Process(pid)
        # print(pid, p.name())
        if p.name() == name:
            pids.append(pid)

    for pid in pids:
        p = psutil.Process(pid)
        for son in p.children(recursive=True):
            son.terminate()
        p.terminate()


class Crawler:

    def __init__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        chrome_options = webdriver.ChromeOptions()  # 启动浏览器
        chrome_options.add_argument('--test-type --ignore-certificate-errors')  # 关闭https验证
        chrome_options.add_experimental_option('useAutomationExtension', False)  # 关闭 自动化提示
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.maximize_window()
        self.login(cookies)
        self.img_dir = 'image'
        os.makedirs(self.img_dir, exist_ok=True)

    @staticmethod
    def get_postion(img_dir, chunk, canves):
        """
        判断缺口位置
        :param chunk: 缺口图片是原图
        :param canves:
        :return: 位置 x, y
        """
        otemp = chunk
        oblk = canves
        target = cv2.imread(otemp, 0)
        template = cv2.imread(oblk, 0)
        # w, h = target.shape[::-1]
        temp = f'{img_dir}/temp.jpg'
        targ = f'{img_dir}/targ.jpg'
        cv2.imwrite(temp, template)
        cv2.imwrite(targ, target)
        target = cv2.imread(targ)
        target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
        target = abs(255 - target)
        cv2.imwrite(targ, target)
        target = cv2.imread(targ)
        template = cv2.imread(temp)
        result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)
        x, y = np.unravel_index(result.argmax(), result.shape)
        return x, y
        # # 展示圈出来的区域
        # cv2.rectangle(template, (y, x), (y + w, x + h), (7, 249, 151), 2)
        # cv2.imwrite("yuantu.jpg", template)
        # cv2.imshow('Show', template)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    @staticmethod
    def urllib_download(imgurl, imgsavepath):
        """
        下载图片
        :param imgurl: 图片url
        :param imgsavepath: 存放地址
        :return:
        """
        from urllib.request import urlretrieve
        urlretrieve(imgurl, imgsavepath)

    @staticmethod
    def get_track(distance):
        """
        模拟轨迹 假装是人在操作
        :param distance:
        :return:
        """
        # 初速度
        v = 10
        # 单位时间为0.2s来统计轨迹，轨迹即0.2内的位移
        t = 0.2
        # 位移/轨迹列表，列表内的一个元素代表0.2s的位移
        tracks = []
        # 当前的位移
        current = 0
        # 到达mid值开始减速
        mid = distance * 7 / 8

        distance += 10  # 先滑过一点，最后再反着滑动回来
        # a = random.randint(1,3)
        while current < distance:
            if current < mid:
                # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
                a = randint(6, 9)  # 加速运动
            else:
                a = -randint(7, 10)  # 减速运动

            # 初速度
            v0 = v
            # 0.2秒时间内的位移
            s = v0 * t + 0.5 * a * (t ** 2)
            # 当前的位置
            current += s
            # 添加到轨迹列表
            tracks.append(round(s))

            # 速度已经达到v,该速度作为下次的初速度
            v = v0 + a * t

        # 反着滑动到大概准确位置
        for i in range(4):
            tracks.append(-randint(2, 3))
        for i in range(4):
            tracks.append(-randint(1, 3))
        return tracks

    def crawler(self, url):
        self.driver.get(url)
        time.sleep(1)
        self.driver.switch_to.frame(self.driver.find_element_by_id('tcaptcha_iframe'))  # switch 到 滑块frame
        time.sleep(0.5)
        bk_block = self.driver.find_element_by_xpath('//img[@id="slideBg"]')  # 大图
        web_image_width = bk_block.size
        web_image_width = web_image_width['width']
        bk_block_x = bk_block.location['x']

        slide_block = self.driver.find_element_by_xpath('//img[@id="slideBlock"]')  # 小滑块
        slide_block_x = slide_block.location['x']

        bk_block = self.driver.find_element_by_xpath('//img[@id="slideBg"]').get_attribute('src')  # 大图 url
        slide_block = self.driver.find_element_by_xpath('//img[@id="slideBlock"]').get_attribute('src')  # 小滑块 图片url
        slid_ing = self.driver.find_element_by_xpath('//div[@id="tcaptcha_drag_thumb"]')  # 滑块

        self.urllib_download(bk_block, f'{self.img_dir}/bkBlock.png')
        self.urllib_download(slide_block, f'{self.img_dir}/slideBlock.png')
        time.sleep(0.5)
        img_bkblock = Image.open(f'{self.img_dir}/bkBlock.png')
        real_width = img_bkblock.size[0]
        width_scale = float(real_width) / float(web_image_width)
        position = self.get_postion(self.img_dir, f'{self.img_dir}/bkBlock.png', f'{self.img_dir}/slideBlock.png')
        real_position = position[1] / width_scale
        real_position = real_position - (slide_block_x - bk_block_x)
        ActionChains(self.driver).click_and_hold(on_element=slid_ing).perform()  # 点击鼠标左键，按住不放
        time.sleep(0.5)
        # print('第二步,拖动元素')
        if randint(1, 10) < 8:  # 模拟滑动
            track_list = self.get_track(real_position + 4)
            for track in track_list:
                ActionChains(self.driver).move_by_offset(xoffset=track, yoffset=0).perform()  # 鼠标移动到距离当前位置（x,y）
                time.sleep(0.002)
        else:  # 直接滑动
            ActionChains(self.driver).move_by_offset(xoffset=real_position, yoffset=0).perform()  # 微调，根据实际情况微调
        time.sleep(1)
        # print('第三步,释放鼠标')
        ActionChains(self.driver).release(on_element=slid_ing).perform()
        time.sleep(1)
        window = self.driver.current_window_handle
        self.driver.switch_to.window(window)
        time.sleep(1)
        rows = BeautifulSoup(self.driver.page_source, 'lxml').find_all('div', class_="col-md-1")
        nums = [int(row.text) for row in rows]
        return nums

    def login(self, cookies):
        # cookies登陆
        loginurl = "http://www.glidedsky.com/login"
        target_url = "http://www.glidedsky.com/"

        if isinstance(cookies, str):
            cookies = dict([i.strip().split('=', 1) for i in cookies.split(';')])

        self.driver.get(loginurl)
        self.driver.delete_all_cookies()
        time.sleep(2)
        for name, value in cookies.items():
            kv = {
                'name': name,
                'value': value,
            }
            self.driver.add_cookie(kv)
        time.sleep(2)
        self.driver.get(target_url)

    def main(self, urls, result_path):
        with open(result_path, 'r') as f:
            dt = json.load(f)
        for url in urls:
            for _ in range(20):
                try:
                    scores = self.crawler(url)
                except:
                    continue
                if scores:
                    print(f"第{url.split('=')[-1]}页 合计:{sum(scores)} 明细:{scores}")
                    dt[url] = sum(scores)
                    with open(result_path, 'w') as f:
                        json.dump(dt, f)
                    break

    def __del__(self):
        self.driver.quit()
        shutil.rmtree(self.img_dir)


if __name__ == '__main__':
    kill_process('chromedriver.exe')  # 关闭残留进程
    result_path = f'crawler-captcha-1.json'
    if not os.path.exists(result_path):
        with open(result_path, 'w') as f:
            json.dump({}, f)

    with open(result_path, 'r') as f:
        dt = json.load(f)

    urls = []
    for i in range(1, 1001):
        url = f'http://www.glidedsky.com/level/web/crawler-captcha-1?page={i}'
        urls.append(url)

    for key, value in dt.items():
        if value > 0:
            urls.remove(key)

    if not urls:
        print(sum(dt.values()))
    else:
        print(f"剩余待采集页数:{len(urls)}")
        Crawler().main(urls, result_path)
