from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class Luntan_homepage3(BasePage):
    #用户登录
    luntan_homepage3_login1_search_loc=(By.CSS_SELECTOR,'.y #ls_username')
    luntan_homepage3_login2_search_loc=(By.CSS_SELECTOR,'.y #ls_password')
    luntan_homepage3_login3_search_loc=(By.CSS_SELECTOR,'.fastlg_l .pn em')
    #进行帖子搜索
    luntan_homepage3_search1_input_loc=(By.CSS_SELECTOR,'.scbar_txt_td .xg1')
    luntan_homepage3_search2_input_loc=(By.CSS_SELECTOR,'.scbar_btn_td .pn')
    luntan_homepage3_search3_input_loc=(By.CSS_SELECTOR,'.pbw .xs3 a')
    luntan_homepage3_search4_input_loc=(By.CSS_SELECTOR,'.plc .ts #thread_subject')
    #退出
    luntan_homepage3_button_quit_loc=(By.CSS_SELECTOR,'#um > p:nth-child(2) > a:nth-child(13)')



    def login(self,username,password,content,title):
        # 用户登录
        self.sendkeys(username,*self.luntan_homepage3_login1_search_loc)
        time.sleep(3)
        self.sendkeys(password,*self.luntan_homepage3_login2_search_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage3_login3_search_loc)
        time.sleep(3)

        # 进行帖子搜索
        self.sendkeys(content,*self.luntan_homepage3_search1_input_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage3_search2_input_loc)
        time.sleep(3)
        self.actity1_window()
        time.sleep(3)
        self.click(*self.luntan_homepage3_search3_input_loc)
        time.sleep(3)
        self.actity2_window()
        time.sleep(3)
        self.element_in_title(title,*self.luntan_homepage3_search4_input_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage3_button_quit_loc)





