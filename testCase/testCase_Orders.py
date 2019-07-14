#!/usr/bin/python
# -*- coding: UTF-8 -*-
from common.tools.HTMLTestRunner import HTMLTestRunner
import unittest,requests,datetime,sys,logging,BSTestRunner,time,os
from common.Log import Log
class testCase_Orders(unittest.TestCase):
    u"""�����Խӿڣ�/login"""
    def setUp(self):
        logging.info('-'*5+"begin test"+"-"*5)
    def tearDown(self):
        logging.info('-'*5+"end test"+'-'*5)
    
    def test_loginSuccess(self):
        u"""���Ե�¼�ɹ�"""
        headers = {'content-type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko', 'Accept': 'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*', 'Accept-Language': 'zh-CN'}
        data = {'uname': '187071484771', 'pwd': '123456'}
        re = requests.post(url='http://www.senbaba.cn/login',headers=headers,data=data)
        status_code = re.status_code
        s = str(status_code)
        json = re.text
        logging.info('-'*5+'res_code'+s+'-'*5)
        logging.info('-'*5+'res'+json+'-'*5)
        assert status_code == 200
        assert json['status'] == 'ok'

    def test_loginFailed(self):
        u"""���Ե�¼ʧ��"""
        headers = {'content-type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko', 'Accept': 'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*', 'Accept-Language': 'zh-CN'}
        data = {'uname': '187071484771', 'pwd': '123457'}
        re = requests.post(url='http://www.senbaba.cn/login1',headers=headers,data=data)
        status_code = re.status_code
        s = str(status_code)
        json = re.text
        logging.info('-'*5+'res_code'+s+'-'*5)
        logging.info('-'*5+'res'+json+'-'*5)
        assert status_code == 200
        assert json['status'] == 'ok'

if __name__ == "__main__":
    unittest.main()
    """
    #���UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 97: ordinal not in range(128)
    reload(sys)
    sys.setdefaultencoding('utf8')
    #������Լ�
    suite = unittest.TestSuite()
    
    suite.addTest(testCase_Orders("test_loginSuccess"))

    suite.addTest(testCase_Orders("test_loginFailed"))

    #����dateΪ���ڣ�timeΪʱ��
    date=time.strftime("%Y%m%d")
    time1=time.strftime("%H%M%S")
    now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    #����·��
    path='F:/test/study/yaml/test_log/'+now+"/"
    #������ִ��ʱ��·���Ѵ��ڵĴ���
    try:
        os.makedirs(path)
    except:
        if path!= None:
            logging.error(u'��ǰ·���Ѿ�����')
    filename=path+'Report.html'
    fp=file(filename,'wb')
    #��־��¼
    Log.log()
    #ִ�в���
    filename = r"./report/test.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Hello World!',
                            description='result: ',
                            tester='expert bugger')
    runner.run(discover)
    fp.close()

    """
