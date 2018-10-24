from pageobjects.base import BasePage
from selenium.webdriver.common.by import By


class Yonghu_huitie(BasePage):
     #»ØÌû
     yonghu_huitie_reply1_input_loc=(By.CSS_SELECTOR,'.pob em a')
     yonghu_huitie_reply2_input_loc=(By.CSS_SELECTOR,'.area #postmessage')
     yonghu_huitie_reply3_input_loc=(By.CSS_SELECTOR,'.pn')

     def reply(self,content):
         self.click(*self.yonghu_huitie_reply1_input_loc)
         self.sendkeys(content,*self.yonghu_huitie_reply2_input_loc)
         self.click(*self.yonghu_huitie_reply3_input_loc)


