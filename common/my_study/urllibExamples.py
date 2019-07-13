#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar
import ssl
# 解决某些环境下报<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
ssl._create_default_https_context = ssl._create_unverified_context

#使用http.cookiejar.CookieJar()创建CookieJar对象
cjar=http.cookiejar.CookieJar()
#使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象
cookie=urllib.request.HTTPCookieProcessor(cjar)
opener=urllib.request.build_opener(cookie)
#将opener安装为全局
urllib.request.install_opener(opener)

def testGet(parameters={}):
    import urllib.request
    params = urllib.urlencode(parameters)
    url = 'https://www.jianshu.com?'+ params
    # 增加header
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }
    req = urllib.request.Request(url)
    response = opener.open(req)
    print(req.get_method())
    print(response.read())


def testPost(parameters):

    params = urllib.urlencode(parameters)
    url="https://github.com/session"
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }
    print('url', url)
    req = urllib.request.Request(url, params.encode('utf-8'))
    response = opener.open(req)



def test_url_parse():
    from urllib import parse
    x = parse.quote('山西', encoding='gb18030')# encoding='GBK
    print(x)  #%C9%BD%CE%F7
    city = parse.unquote('%E5%B1%B1%E8%A5%BF',)  # encoding='utf-8'
    print(city)  # 山西

def testURLError():
    import urllib.error
    import urllib.request
    requset = urllib.request.Request('http://www.usahfkjashfj.com/')
    try:
        urllib.request.urlopen(requset).read()
    except urllib.error.URLError as e:
        print(e.reason)
    else:
        print('success')

def proxy_test():
    import urllib.request
    url = 'http://httpbin.org/ip'
    proxy = {'http':'39.134.108.89:8080','https':'39.134.108.89:8080'}
    proxies = urllib.request.ProxyHandler(proxy) # 创建代理处理器
    opener = urllib.request.build_opener(proxies,urllib.request.HTTPHandler) # 创建特定的opener对象
    urllib.request.install_opener(opener) # 安装全局的opener 把urlopen也变成特定的opener
    data = urllib.request.urlopen(url)
    print(data.read().decode())

