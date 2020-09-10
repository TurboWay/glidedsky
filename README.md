# glidedsky
glidedsky 爬虫练习笔记

![image](https://github.com/TurboWay/imgstore/blob/master/glidedsky/process.jpg)

# note

- 爬虫采集属于 io 密集型操作，使用多线程并发可以提高效率，但是最佳并发数取决于爬虫的机器配置，而不是越多越好
- 网络请求有时候会出错，重试是必要的，不用框架的话，装饰器是很好的选择
- 使用代理 ip 时，网络错误导致漏爬的可能性很高，只有重试是不够的，先把结果存下来，做好补爬的准备，是比较稳妥的策略

## list
| 代码 | 说明  | 
| ------------ | ------------ |
| [crawler-basic-1.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-basic-1.py)       | 爬虫-基础1 |
| [crawler-basic-2.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-basic-2.py)       | 爬虫-基础2 |
| [crawler-captcha-1.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-captcha-1.py)       | 爬虫-验证码-1 【未开始】 |
| [crawler-css-puzzle-1.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-css-puzzle-1.py)       | 爬虫-CSS反爬 |
| [crawler-font-puzzle-1.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-font-puzzle-1.py)       | 爬虫-字体反爬-1 |
| [crawler-font-puzzle-2.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-font-puzzle-2.py)       | 爬虫-字体反爬-2 |
| [crawler-ip-block-1.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-ip-block-1.py)       | 爬虫-IP屏蔽1 |
| [crawler-ip-block-2.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-ip-block-2.py)       | 爬虫-IP屏蔽2 |
| [crawler-javascript-obfuscation-1.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-javascript-obfuscation-1.py)       | 爬虫-JS加密1 |
| [crawler-sprite-image-1.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-sprite-image-1.py)       | 爬虫-雪碧图-1 |
| [crawler-sprite-image-2.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-sprite-image-2.py)       | 爬虫-雪碧图-2 【未开始】 |
