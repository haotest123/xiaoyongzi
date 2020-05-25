from framework.browser_engine import BrowserEngine
import unittest
import time
class base_testcase(unittest.TestCase):
    def setUp(self):
        browser=BrowserEngine()
        self.driver=browser.open_browser()


    def tearDown(self):
        time.sleep(5)
        #self.driver.quit()



