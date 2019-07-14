#!/usr/bin/python
# -*- coding: UTF-8 -*-
from string import Template
import os
#https://blog.csdn.net/smj811504083/article/details/78250002
testcase_dir=r"./testCase"
try:
    os.mkdir(testcase_dir)
except:
    pass
def oneMethodCreate(MethodList,interfaceNamePara):
    code=Template('''\n    def test_${testcase}(self):
        u"""${description}"""
        headers = $headers
        data = $data
        re = requests.$method(url='$url',headers=headers,data=data)
        status_code = re.status_code
        s = str(status_code)
        json = re.text
        logging.info('-'*5+'res_code'+s+'-'*5)
        logging.info('-'*5+'res'+json+'-'*5)
        assert status_code == 200
        assert json['status'] == 'ok'
''')

    string = code.substitute(testcase=MethodList["testcase"],description=MethodList["description"],
                             method=MethodList['method'],url=MethodList['url'],headers=MethodList['headers'],data=MethodList['data'],
                             )
    return string

def manymethodCreate(MethodParaList,interfaceNamePara):
    string = ""
    for MethodPara in MethodParaList:
        string2=oneMethodCreate(MethodPara,interfaceNamePara)
        string=string+string2
    return string

def oneTestsuitCreate(MethodList,parameters):
    code = Template('''suite.addTest(${className}("test_${testcase}"))''')
    string = code.substitute(testcase = MethodList["testcase"],className = parameters[0])
    return string


def addtestsuit(parameters):
    string = ""
    temp = Template('''\n    suite.addTest(${className}("test_${testcase}"))
''')
    num = len(parameters[2])
    for i in range(0,num):

        testcasei = parameters[2][i]['testcase']
        string2 = temp.substitute(className = parameters[0]['className'],testcase = testcasei)
        string=string+string2
    # print (string)
    return string

##################################
##################################################################################################

def modelClassCreate(parameters):

    modelCode = manymethodCreate(parameters[2],parameters[1])
    adtestsuit = addtestsuit(parameters)
    code = Template('''#!/usr/bin/python
# -*- coding: UTF-8 -*-
from common.tools.HTMLTestRunner import HTMLTestRunner
import unittest,requests,datetime,sys,logging,BSTestRunner,time,os
from common.Log import Log
class ${className}(unittest.TestCase):
    u"""待测试接口：${interfaceName}"""
    def setUp(self):
        logging.info('-'*5+"begin test"+"-"*5)
    def tearDown(self):
        logging.info('-'*5+"end test"+'-'*5)
    ${model}
if __name__ == "__main__":
    unittest.main()
    """
    #解决UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 97: ordinal not in range(128)
    reload(sys)
    sys.setdefaultencoding('utf8')
    #构造测试集
    suite = unittest.TestSuite()
    ${testsuite}
    #定义date为日期，time为时间
    date=time.strftime("%Y%m%d")
    time1=time.strftime("%H%M%S")
    now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    #创建路径
    path='F:/test/study/yaml/test_log/'+now+"/"
    #解决多次执行时报路径已存在的错误
    try:
        os.makedirs(path)
    except:
        if path!= None:
            logging.error(u'当前路径已经存在')
    filename=path+'Report.html'
    fp=file(filename,'wb')
    #日志记录
    Log.log()
    #执行测试
    filename = r"./report/test.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Hello World!',
                            description='result: ',
                            tester='expert bugger')
    runner.run(discover)
    fp.close()

    """
''')

    str_suite = addtestsuit(parameters)
    print(str_suite)
    fileStr = code.substitute(className=parameters[0]["className"],interfaceName=parameters[1]['interfacename'],testsuite=str_suite,model=modelCode)
    f=open(os.path.join(testcase_dir,parameters[0]["className"]+".py"),'w')
    f.write(fileStr)
    f.close()


################################################################
parameters=[ {"className":"testCase_Orders"},
             {"interfacename":"/login"},
                [
                   {#########################################1
                        "description":u"测试登录成功",
                        "method":"post",
                        "url":"http://www.senbaba.cn/login",
                        "headers":{'content-type': 'application/json',
                        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                        'Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*',
                        'Accept-Language':'zh-CN'},
                        "data":{"uname":"187071484771","pwd":"123456"},
                        "testcase":"loginSuccess"
                    },

                  {#########################################2
                        "description":u"测试登录失败",
                        "method":"post",
                        "url":"http://www.senbaba.cn/login1",
                        "headers":{
                        'content-type': 'application/json',
                        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                        'Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*',
                        'Accept-Language':'zh-CN'
                                  },
                        "data":{"uname":"187071484771","pwd":"123457"},
                        "testcase":"loginFailed"
                   }
                ]
           ]

MethodParaList=parameters[2]
print(MethodParaList)
modelClassCreate(parameters)