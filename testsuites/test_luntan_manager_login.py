from testsuites.base_testcase import Base_testcase
from pageobjects.yonghu_login import Yonghu_login
import unittest
import time

class Luntan_manager_login(Base_testcase):
    def test_1untan_manager_login(self):
        yonghu_login=Yonghu_login(self.driver)
        yonghu_login.login('admin','haotest')
        time.sleep(3)
        yonghu_login.moren()
        #删除帖子





if __name__ == '__main__':
    unittest.main()

