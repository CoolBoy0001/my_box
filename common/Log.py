#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import common.readConfig as readConfig
import logging
import threading
import datetime
class Log:
    def __init__(self):
        global logPath, resultPath, proDir
        proDir = readConfig.proDir
        resultPath = os.path.join(proDir, "result")


        # create result file if it doesn't exist
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        # defined test result file name by localtime
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        logging.basicConfig(
            # 日志级别
            level=logging.INFO,
            # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
            format='%(asctime)s %(filename)s[line: %(lineno)d] %(levelname)s %(message)s',
            # 打印日志的时间
            datefmt='%a, %d %b %Y %H:%M:%S',
            # 日志文件存放的目录及日志文件名
            filename=logPath,
            # 打开日志的方式
            filemode='w'
        )


        # create test result file if it doesn't exist
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        # defined logger
        self.logger = logging.getLogger()
        # defined log level
        self.logger.setLevel(logging.INFO)

        # defined handler
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        # defined formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # defined formatter
        handler.setFormatter(formatter)
        # add handler
        self.logger.addHandler(handler)

class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log