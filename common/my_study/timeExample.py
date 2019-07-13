#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import time  # 引入time模块
import datetime
ticks = time.time()
print ("当前时间戳为:", ticks)
localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)

print( time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)
d1 = datetime.datetime.now()
d1.strftime("%Y-%m-%d %H:%M:%S")
d2 = d1 + datetime.timedelta(seconds=10)#增加10秒
d2.strftime("%Y-%m-%d %H:%M:%S")
d2 = d1 + datetime.timedelta(minutes=10)#增加10分钟
d2.strftime("%Y-%m-%d %H:%M:%S")
d2 = d1 + datetime.timedelta(hours=10)#增加10小时
d2 = d1 + datetime.timedelta(days=10)#增加10天
d2 = d1 - datetime.timedelta(days=10)#减去10天
