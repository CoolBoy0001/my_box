#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import json
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
data = {"bs":"pythonrequests的用法" }
response = requests.get('http://www.baidu.com',headers=headers,data=data)
# print(response.status_code)
# print(response.url)
# print(response.headers)
# print(response.cookies)
# print(response.content)
#################################################################
data = {'name':'tom','age':'22'}
response = requests.post('http://httpbin.org/post', data=data,headers=headers)
# print((response.text))
# print(json.dumps(response.text))
#################################################
import requests
session = requests.Session()
session.get('http://httpbin.org/cookies/set/number/12345')
response = session.get('http://httpbin.org/cookies')
# print(response.text)
##############################################
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
response = requests.get('https://www.12306.cn',verify=False)
# print(response.status_code)
#######################################################
import requests
from requests.exceptions import ReadTimeout

try:
    res = requests.get('http://httpbin.org', timeout=0.1)
    print(res.status_code)
except ReadTimeout:
    print("timeout")
###############################################################
###proxy
import requests

proxies={
    'http':'http://127.0.0.1:7078',
    'https':'https://127.0.0.1:7078'
}

response=requests.get('https://www.taobao.com',proxies=proxies)
j = response.json()
print(response.status_code)
##############################################################
# 上传文件
files = {'picture': open('baidu.png', 'rb')}
response = requests.post('http://httpbin.org/post', files=files)
print(response.text)

