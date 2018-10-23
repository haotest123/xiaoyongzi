from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

class PageLogin(BasePage):
    #查找登录操作页面用到的元素
    login_page_usernamr_input_loc=(By.CLASS_NAME,'android.widget.EditText')
    login_page_password_input_loc=(By.ID,'com.example.todolist:id/passwordET')
    login_page_login_input_loc=(By.CLASS_NAME,'android.widget.Button')

    def login(self,username,password):
        self.sendkeys(username,*self.login_page_usernamr_input_loc)
        self.sendkeys(password,*self.login_page_password_input_loc)
        self.click(*self.login_page_login_input_loc)









