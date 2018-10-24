
import HTMLTestRunner
import unittest
import os
import time

report_path = os.path.dirname(os.path.abspath('.'))+ '/test_report/'
now = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
HtmlFile = report_path+now+'_result.html'
fp = open(HtmlFile,'wb')
# test_dir='./'
#加载所有以test开头的.py文件
suite=unittest.TestLoader().discover('testsuites',pattern='test*.py')

if __name__=='__main__':
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'Web UI自动化测试报告，测试结果如下',description=u'用例测试情况如下')
    runner.run(suite)
    fp.close()
