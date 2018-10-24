from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class Luntan_homepage4(BasePage):
#用户登录
    luntan_homepage4_login1_search_loc=(By.CSS_SELECTOR,'.y #ls_username')
    luntan_homepage4_login2_search_loc=(By.CSS_SELECTOR,'.y #ls_password')
    luntan_homepage4_login3_search_loc=(By.CSS_SELECTOR,'.fastlg_l .pn em')
#点击默认板块
    luntan_homepage4_moren_search_loc=(By.CSS_SELECTOR,'.bm_c tbody tr td h2 a')
 # 点击发帖
    luntan_homepage4_fatie_search_loc=(By.CSS_SELECTOR,'.mn >*:nth-child(3) #newspecial')
# 点击发起投票，开始输入投票内容
    luntan_homepage4_toupiao_search_loc=(By.CSS_SELECTOR,'#ct div .tb li:last-child a')

    luntan_homepage4_title_search_loc=(By.CSS_SELECTOR,'#postbox .pbt .z span input')
    luntan_homepage4_content1_search_loc=(By.CSS_SELECTOR,'.exfm .sinf #pollm_c_1 p input')
    luntan_homepage4_content2_search_loc=(By.CSS_SELECTOR,'.exfm .sinf #pollm_c_1 p:nth-child(2) input')
    luntan_homepage4_content3_search_loc=(By.CSS_SELECTOR,'.exfm .sinf #pollm_c_1 p:nth-child(3) input')
#点击发起投票按钮开始投票
    luntan_homepage4_start_search_loc=(By.CSS_SELECTOR,'.mtm button')
# 点击单选投票按钮
    luntan_homepage4_select_search_loc=(By.CSS_SELECTOR,'.pslt input')
# 点击提交按钮
    luntan_homepage4_button_search_loc=(By.CSS_SELECTOR,'.pcht tbody tr:last-child button')


    luntan_homepage4_button1_quit_loc=(By.CSS_SELECTOR,'.pl table tr td:last-child span')

    luntan_homepage4_button2_search_loc=(By.CSS_SELECTOR,'.pcht tbody tr .pvt label')

    luntan_homepage4_button3_search_loc=(By.CSS_SELECTOR,'.pcht tbody tr:nth-child(2) td:last-child')




    def login(self,username,password,title,content1,content2,content3):
    # 用户登录
        self.sendkeys(username,*self.luntan_homepage4_login1_search_loc)
        time.sleep(3)
        self.sendkeys(password,*self.luntan_homepage4_login2_search_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage4_login3_search_loc)
        time.sleep(3)
    # 点击默认板块
        self.click(*self.luntan_homepage4_moren_search_loc)
        time.sleep(3)
      # 点击发帖
        self.click(*self.luntan_homepage4_fatie_search_loc)
    # 点击发起投票，开始输入投票内容
        self.click(*self.luntan_homepage4_toupiao_search_loc)
        time.sleep(3)
        self.sendkeys(title,*self.luntan_homepage4_title_search_loc)
        time.sleep(3)
        self.sendkeys(content1,*self.luntan_homepage4_content1_search_loc)
        time.sleep(3)
        self.sendkeys(content2,*self.luntan_homepage4_content2_search_loc)
        time.sleep(3)
        self.sendkeys(content3,*self.luntan_homepage4_content3_search_loc)
        time.sleep(3)
    # 点击发起投票按钮开始投票
        self.click(*self.luntan_homepage4_start_search_loc)
        time.sleep(3)
    # 点击单选投票按钮
        self.click(*self.luntan_homepage4_select_search_loc)
        time.sleep(3)
    # 点击提交按钮
        self.click(*self.luntan_homepage4_button_search_loc)
        time.sleep(5)

        self.element_output_title(*self.luntan_homepage4_button1_quit_loc)
        time.sleep(5)
        self.element_output_title(*self.luntan_homepage4_button2_search_loc)
        time.sleep(5)
        self.element_output_title(*self.luntan_homepage4_button3_search_loc)



