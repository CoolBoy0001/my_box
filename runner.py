# coding: utf-8
__author__ = 'Administrator'
import unittest

from common.tools.HTMLTestRunner import HTMLTestRunner
start_dir=r"./testCase"
filename = r"./report/test.html"  # 定义报告存放路径

def dependencies():
    cmdline=["python setup.py build","python setup.py sdist","python setup.py install"]
    import os
    for cmd in cmdline:
        os.system(cmd)

def runAllCases():
    discover = unittest.defaultTestLoader.discover(start_dir = start_dir,pattern='test*.py')
    if __name__ == "__main__":
        print(filename)
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(stream=fp,
                                title='Hello World!',
                                description='result: ',
                                tester='expert bugger')
        runner.run(discover)
        fp.close()

dependencies()
# runAllCases()