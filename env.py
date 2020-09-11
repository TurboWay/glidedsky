#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/9/8 12:20
# @Author : way
# @Site : 
# @Describe:


cookies = '__gads=ID=227efba24e897ba1:T=1599208355:S=ALNI_MbtWcmS-lrKu_DASa8CKA1pf9SuRQ; _ga=GA1.2.280986667.1599208355; _gid=GA1.2.1720620895.1599449018; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1599526906,1599614065,1599711534,1599786061; footprints=eyJpdiI6IkI3NjNHZWI3MUZ0NndGRmdRenRJR1E9PSIsInZhbHVlIjoienVGb3dRTngxZlpxcEUxbmZjTFRzS1FmWFNhUzNERFwvSWtMNjQxdjNyMjMwc3VcL2RkY2tCNnZjZjBaMFlkZGczIiwibWFjIjoiZjlkOTMzZDUxOTVjOGUwOTVkZGNjOGYzNjFmNjQwY2FlZWU2MzYzYjliZGE1MDNlNmYyZjE0NDdkY2RjY2VjYiJ9; _gat_gtag_UA_75859356_3=1; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjM3bXg0a1J6b0VmNkl3ZThwdnVYRXc9PSIsInZhbHVlIjoiZXQ2K3NRUGp0clJwM3JoSkpJdGQ5UklBckE0ZWZsTmFhS3d4UVgzSGUwcUltMjdQNHB3NkV0eHZRXC9WUmxlcnJJR2dUckNOa2dXemtoRk5xeFlmUXdEcUlWWExRWndURG1aWkF6UjBXUjB5YTIzTzBWdEcxUjhMdmJsczVqNGthYWpcL1RIRGZPMUdzOUVSZjRaVlBnaGZxeTB1U0dRRjBRdmJPZFJwN2VXdTQ9IiwibWFjIjoiMGE0ZmJmY2YwYTM3ODIyNjdiNDUwZDJlZmEwNzY0M2E2ZjBmYWE3M2Q1ZjliYmM3ZjhlZDZiZmMxN2RmMjkwNiJ9; XSRF-TOKEN=eyJpdiI6ImFMMUVDVTF4cW4rcnpSZklWVDE0aEE9PSIsInZhbHVlIjoiQytMRnpTYloxOFk3NHlnaDlZRGhBQlBoTEpXczNoaFZJZDZaRnBRd01zeHVEdnRyaWtod2dZaHpma3VQczZxdSIsIm1hYyI6ImRhMWM5MDU0NmE1OTM3M2QzMjRkMWQwNzFmMDU0NmJkZjgyMTkwNmVmODFjZThhOGU3ZmUyYTI2M2ExZGVkNWMifQ%3D%3D; glidedsky_session=eyJpdiI6IjhSdEpWbGRZcGpNcFlUQzkxeVN6eFE9PSIsInZhbHVlIjoiUHozWXFCT0RcL3JEWHNwMmFGV2U5ZzlPaVZIdlN2TVlhVjFISWcrdCtcL1dGaHY1eDkwNUxoU29XKzZzS2kwZ2VvIiwibWFjIjoiMmUzMDgyMjlmYzZhYzFkMTU3MTY2ZTAzNzQ3NmQ0ZjdiMzM4M2Y3NDk0Nzc4ZTA2NmFlMjI2N2VmOWYxODdhZiJ9; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1599790277'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': cookies,
    'Host': 'www.glidedsky.com',
    'Referer': 'http://www.glidedsky.com/level/web/crawler-basic-2?page=1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
}

# 代理 ip 使用了 阿布云 https://center.abuyun.com/

# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "your proxyUser"
proxyPass = "your proxyPass"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}

