from framework.browser_engine import BrowserEngine
import unittest
import time


class Base_testcase(unittest.TestCase):
    def setUp(self):
        #setUp()中的代码  主要是测试的前期准备工作
        browser= BrowserEngine()
        self.driver=browser.open_browser()
        # self.driver=webdriver.Chrome('../tools/chromedriver.exe')
        # self.driver.implicitly_wait(5)
        # time.sleep(3)

    def tearDown(self):
    # tearDown()中的代码  主要是测试结束后要做的工作
        time.sleep(5)
        self.driver.quit()