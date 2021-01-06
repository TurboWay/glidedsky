# glidedsky
glidedsky 通关笔记

[镀金的天空](http://www.glidedsky.com/) 是一个互联网技能认证网站，要保证用户解出一道题目就意味着拥有了解决类似问题相应的技能

![image](https://github.com/TurboWay/imgstore/blob/master/glidedsky/process.jpg)

## wish

- 作为过来人，深知个人自学的艰难，尤其是无人指导、无人探讨的孤独者。本 repo 旨在提供一份参考答案、解题思路，希望您可以在解题过程中有所收获。

## note

- 爬虫采集属于 io 密集型操作，使用多线程并发可以提高效率，但是最佳并发数取决于爬虫的机器配置，而不是越多越好
- 网络请求有时候会出错，重试是必要的，不用框架的话，装饰器是很好的选择
- 使用代理 ip 时，网络错误导致漏爬的可能性很高，只有重试是不够的，先把结果存下来，做好补爬的准备，是比较稳妥的策略
- 使用图片识别时，成功率不会达到 100%，所以多采集几次是必要的，对每个数取重复率最高的结果，是较好的做法

## list
| 代码 | 说明 |
| ------------ | ------------ |
| [crawler-basic-1.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-basic-1.py)       | 爬虫-基础1 |
| [crawler-basic-2.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-basic-2.py)       | 爬虫-基础2 |
| [crawler-captcha-1.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-captcha-1.py)       | 爬虫-验证码-1 |
| [crawler-captcha-2.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-captcha-2.py)       | 爬虫-验证码-2 【网站服务异常，暂时无法审题】 |
| [crawler-css-puzzle-1.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-css-puzzle-1.py)       | 爬虫-CSS反爬 |
| [crawler-font-puzzle-1.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-font-puzzle-1.py)       | 爬虫-字体反爬-1 |
| [crawler-font-puzzle-2.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-font-puzzle-2.py)       | 爬虫-字体反爬-2 |
| [crawler-ip-block-1.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-ip-block-1.py)       | 爬虫-IP屏蔽1 |
| [crawler-ip-block-2.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-ip-block-2.py)       | 爬虫-IP屏蔽2 |
| [crawler-javascript-obfuscation-1.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-javascript-obfuscation-1.py)       | 爬虫-JS加密1 |
| [crawler-sprite-image-1.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-sprite-image-1.py)       | 爬虫-雪碧图-1 |
| [crawler-sprite-image-2.py](https://github.com/TurboWay/glidedsky/blob/master/crawler-sprite-image-2.py)       | 爬虫-雪碧图-2 |

## refer
>滑动验证码 参考 https://github.com/ybsdegit/captcha_qq
>
>图片识别模型训练 https://github.com/TurboWay/antman
