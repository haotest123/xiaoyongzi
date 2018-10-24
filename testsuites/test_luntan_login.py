from testsuites.base_testcase import Base_testcase
from pageobjects.yonghu_login import Yonghu_login
from pageobjects.yonghu_fatie import Yonghu_fatie
from pageobjects.yonghu_huitie import Yonghu_huitie
import unittest
import time


class Luntan_login(Base_testcase):
    def test_1untan_login(self):
        #登录
        yonghu_login=Yonghu_login(self.driver)
        yonghu_login.login('anyong','868686')
        time.sleep(3)
        #进入默认板块
        yonghu_login.moren()
        time.sleep(3)
        #发帖
        yonghu_fatie=Yonghu_fatie(self.driver)
        yonghu_fatie.publish('天气','在北京真是太热烈了，热热热')
        time.sleep(3)
        #回帖
        yonghu_huitie=Yonghu_huitie(self.driver)
        yonghu_huitie.reply('天气非常好，心情也很舒适')
        time.sleep(3)
        #退出
        yonghu_login.quit()


if __name__ == '__main__':
    unittest.main()

        # self.driver.find_element_by_css_selector('.y #ls_username').send_keys('anyong')
        # time.sleep(3)
        # self.driver.find_element_by_css_selector('.y #ls_password').send_keys('868686')
        # time.sleep(3)
        # self.driver.find_element_by_css_selector('.fastlg_l .pn em').click()
        # time.sleep(3)



