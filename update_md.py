#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/9 16:44
# @Author : way
# @Site : 
# @Describe: 用于更新 md 索引

md = """# glidedsky
glidedsky 爬虫练习笔记

![image](https://github.com/TurboWay/imgstore/blob/master/glidedsky/process.jpg)

# note

- 爬虫采集属于 io 密集型操作，使用多线程并发可以提高效率，但是最佳并发数取决于爬虫的机器配置，而不是越多越好
- 网络请求有时候会出错，重试是必要的，不用框架的话，装饰器是很好的选择
- 使用代理 ip 时，网络错误导致漏爬的可能性很高，只有重试是不够的，先把结果存下来，做好补爬的准备，是比较稳妥的策略
- 使用图片识别时，成功率不会达到 100%，所以多采集几次是必要的，对每个数取重复率最高的结果，是较好的做法

## list
| 代码 | 说明  | 
| ------------ | ------------ |
"""

import re
import os

for demo in os.listdir():
    if demo.startswith('crawler') and demo.endswith('py'):
        with open(demo, 'r', encoding='utf-8') as f:
            desc = re.findall("@Describe:(.*)", f.read())
        desc = desc[0].strip() if desc else ''
        str = f"| [{demo}](https://github.com/TurboWay/glidedsky/blob/master/{demo})       | {desc} |\n"
        md += str

with open("README.md", 'w', encoding='utf-8') as f:
    md += """
## refer
>滑动验证码 参考 https://github.com/ybsdegit/captcha_qq
>
>图片识别 参考 https://zhuanlan.zhihu.com/p/80995795
>
>模型下载链接: https://pan.baidu.com/s/1y6CQHErGVkmlP4KzoSRkpw 提取码: 8yvd 
"""
    f.write(md)