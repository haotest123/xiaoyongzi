from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time


class Luntan_homepage2(BasePage):


    luntan_homepage2_button4_loc=(By.CSS_SELECTOR,'.fastlg_l .pn')
    luntan_homepage2_input_input_loc = (By.CSS_SELECTOR, 'td .px')
    luntan_homepage2_password_input_loc = (By.CSS_SELECTOR, '.c div:nth-of-type(2) .px')
    luntan_homepage2_button_input_loc = (By.CSS_SELECTOR, 'td .pn')

    # 进入默认板块，删除帖子
    luntan_homepage2_a_input_loc = (By.CSS_SELECTOR, '.fl_tb h2 a')
    #删除帖子
    luntan_homepage2_onclick_input_loc=(By.CSS_SELECTOR,'.o input')
    luntan_homepage2_onclick2_input_loc=(By.CSS_SELECTOR,'#mdly p strong a')
    luntan_homepage2_button2_input_loc=(By.CSS_SELECTOR,'.tm_c #moderateform .o button')
    #退出
    luntan_homepage2_span_input_loc = (By.CSS_SELECTOR, '.hdc #um p > *:last-child')
    luntan_homepage2_button5_loc = (By.CSS_SELECTOR, '.fastlg .y table tbody tr:last-child td:nth-last-child(2).fastlg_l .pn')
    luntan_homepage2_login1_input_loc = (By.CSS_SELECTOR, 'td .px')
    luntan_homepage2_login2_input_loc = (By.CSS_SELECTOR, '.c div:nth-of-type(2) .px')
    luntan_homepage2_button6_input_loc = (By.CSS_SELECTOR, 'td .pn')

    # 进入版块管理（管理中心---论坛）
    luntan_homepage2_guanli_iuput_loc=(By.CSS_SELECTOR,'#um p:nth-child(2)>*:nth-last-child(3)')
    luntan_homepage2_guanli2_input_loc=(By.CSS_SELECTOR,'#loginform .loginform input')
    luntan_homepage2_guanli3_input_loc=(By.CSS_SELECTOR,'.loginnofloat input')

    # 创建新的版块
    luntan_homepage2_xinde1_input_loc=(By.CSS_SELECTOR,'.nav #topmenu li:nth-child(7) em a')
    luntan_homepage2_xinde2_input_loc=(By.CSS_SELECTOR,'tr:last-child td .board input')
    luntan_homepage2_xinde3_input_loc=(By.CSS_SELECTOR,'.fixsel .btn')

    luntan_homepage2_quit1_input_loc=(By.CSS_SELECTOR,'.uinfo p:first-child a')
    luntan_homepage2_quit2_input_loc=(By.CSS_SELECTOR,'.hdc #um p > *:last-child')

    #登录
    luntan_homepage2_login3_input_loc=(By.CSS_SELECTOR,'.y #ls_username')
    luntan_homepage2_login4_input_loc=(By.CSS_SELECTOR,'.y #ls_password')
    luntan_homepage2_login5_input_loc=(By.CSS_SELECTOR,'.fastlg_l .pn em')
    luntan_homepage2_moren_input_loc=(By.CSS_SELECTOR,'.fl_tb tbody>*:nth-last-child(2) td h2 a')

    # 发帖
    luntan_homepage2_fabiao1_input_loc=(By.CSS_SELECTOR,'.pbt .px')
    luntan_homepage2_fabiao2_input_loc=(By.CSS_SELECTOR,'.area #fastpostmessage')
    luntan_homepage2_fabiao3_input_loc=(By.CSS_SELECTOR,'.ptm #fastpostsubmit')
    luntan_homepage2_fabiao4_input_loc=(By.CSS_SELECTOR,'.pob em a')

    #回帖
    luntan_homepage2_reply1_input_loc=(By.CSS_SELECTOR,'.area #postmessage')
    luntan_homepage2_reply2_input_loc = (By.CSS_SELECTOR, '.o .pn')

    def login(self, username, password,login1,login2,password2,content,title,login3,login4,fabiao1,fabiao2,reply1):
        self.click(*self.luntan_homepage2_button4_loc)
        time.sleep(3)
        self.sendkeys(username,*self.luntan_homepage2_input_input_loc)
        time.sleep(3)
        self.sendkeys(password,*self.luntan_homepage2_password_input_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage2_button_input_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage2_a_input_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage2_onclick_input_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage2_onclick2_input_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage2_button2_input_loc)
        time.sleep(3)

        #退出
        self.click(*self.luntan_homepage2_span_input_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage2_button5_loc)
        time.sleep(3)
        self.sendkeys(login1,*self.luntan_homepage2_login1_input_loc)
        time.sleep(3)
        self.sendkeys(login2, *self.luntan_homepage2_login2_input_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage2_button6_input_loc)
        time.sleep(3)


        #进入管理中心
        self.click(*self.luntan_homepage2_guanli_iuput_loc)
        time.sleep(3)
        self.actity1_window()
        self.sendkeys(password2,*self.luntan_homepage2_guanli2_input_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage2_guanli3_input_loc)
        time.sleep(3)

        #创建新模块
        self.click(*self.luntan_homepage2_xinde1_input_loc)
        time.sleep(3)
        self.in_moudle(content)
        time.sleep(3)
        self.sendkeys(title,*self.luntan_homepage2_xinde2_input_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage2_xinde3_input_loc)
        time.sleep(3)
        self.quit_moudle()
        time.sleep(3)
        self.click(*self.luntan_homepage2_quit1_input_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage2_quit2_input_loc)
        time.sleep(3)
        #登录
        self.sendkeys(login3,*self.luntan_homepage2_login3_input_loc)
        time.sleep(3)
        self.sendkeys(login4,*self.luntan_homepage2_login4_input_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage2_login5_input_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage2_moren_input_loc)
        time.sleep(3)
        #发帖
        self.sendkeys(fabiao1,*self.luntan_homepage2_fabiao1_input_loc)
        time.sleep(3)
        self.sendkeys(fabiao2,*self.luntan_homepage2_fabiao2_input_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage2_fabiao3_input_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage2_fabiao4_input_loc)
        time.sleep(3)
        # 回帖
        self.sendkeys(reply1,*self.luntan_homepage2_reply1_input_loc)
        time.sleep(3)
        self.click(*self.luntan_homepage2_reply2_input_loc)




