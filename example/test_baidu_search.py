from example.baidu_homepage import HomePage
from testsuites.base_testcase import Base_testcase
import unittest
import time

class BaiduSearch(Base_testcase):
    # 测试方法必须要以test开头
    def test_baidu_search(self):
        # 声明HomePage类对象
        home_page = HomePage(self.driver)
        #调用所有页面的公共open_url()方法
        home_page.open_url('http://www.baidu.com')
        time.sleep(2)
        home_page.search('python')
        time.sleep(5)

        # self.driver.find_element_by_id('kw').send_keys('selenium'+Keys.RETURN)
        # time.sleep(2)
        # assert 'selenium' in self.driver.title
if __name__ == '__main__':
    unittest.main()

    #
    # #浏览器返回
    # def back(self):
    #     self.driver.back()
    #     logger.info('此页面点击返回')
    # #浏览器前进
    # def forward(self):
    #     self.driver.forward()
    #     logger.info('此页面点击前进')





