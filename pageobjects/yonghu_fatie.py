from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class Yonghu_fatie(BasePage):
    # ·¢Ìû
    yonghu_fatie_title_input_loc = (By.CSS_SELECTOR, '.pbt #subject')
    yonghu_fatie_content_input_loc = (By.CSS_SELECTOR, '.area #fastpostmessage')
    yonghu_fatie_submit_input_loc = (By.CSS_SELECTOR, '.ptm .pn')

    # ·¢Ìû
    def publish(self,title,content):
        self.sendkeys(title,*self.yonghu_fatie_title_input_loc)
        self.sendkeys(content,*self.yonghu_fatie_content_input_loc)
        self.click(*self.yonghu_fatie_submit_input_loc)


