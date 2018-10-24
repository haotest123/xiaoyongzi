from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class Yonghu_login(BasePage):
    #用户登录
    yonghu_login_username_input_loc=(By.ID,'ls_username')
    yonghu_login_password_input_loc = (By.ID, 'ls_password')
    yonghu_login_button_input_loc=(By.CSS_SELECTOR,'.fastlg_l .pn em')
    # 进入默认板块
    yonghu__moren_input_loc = (By.CSS_SELECTOR, '.fl_tb h2 a')
    #管理中心
    yonghu_guanli_input_loc=(By.CSS_SELECTOR,'')
    # 退出
    yonghu_quit_button_input_loc = (By.CSS_SELECTOR, '.hdc #um p > *:last-child')

    # 用户登录
    def login(self,username,password):
        self.sendkeys(username,*self. yonghu_login_username_input_loc)
        time.sleep(3)
        self.sendkeys(password,*self. yonghu_login_password_input_loc)
        time.sleep(3)
        self.click(*self. yonghu_login_button_input_loc)
    # 退出
    def quit(self):
        self.click(*self.yonghu_quit_button_input_loc)
    # 进入默认板块
    def moren(self):
        self.click(*self.yonghu__moren_input_loc)

