from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.base import BasePage

#继承BasePage类
class HomePage(BasePage):
    # 定位器，通过元素定位元素的对象
    home_page_input_search_loc=(By.ID,'kw')
    home_page_button_search_loc=(By.ID,'su')

    #输入搜索内容，并提交
    def search(self,content):
        self.sendkeys(content,*self.home_page_input_search_loc)
        self.click(*self.home_page_button_search_loc)
