from selenium.webdriver.common.by import By
from PageObjects.base import BasePage
from framework.logger import Logger
import time

#获取一个loger对象，调用getlog()方法:
logger=Logger(logger="jiuzhen").getlog()

class jiuzhen(BasePage):
    #----------------------------------损失类型：一般损伤--------------------------------------------------------------
    # 点选事故类型
    jiuzhen_homepage1_input_input1_loc = (By.CSS_SELECTOR, 'html body #baseInfor table tr:nth-child(5) td:nth-child(2) option:nth-child(2)')
    # 点选损失类型为：一般损伤
    jiuzhen_homepage1_button_button1_loc = (By.CSS_SELECTOR, 'html body #baseInfor table tr:nth-child(5) td:nth-child(4) option:nth-child(3)')
    # 点选损失类型为：伤残
    jiuzhen_homepage1_button_button5_loc=(By.CSS_SELECTOR,'html body #baseInfor table tr:nth-child(5) td:nth-child(4) option:nth-child(4)')
    # 点选损失类型为：死亡
    jiuzhen_homepage1_button_button6_loc = (By.CSS_SELECTOR, 'html body #baseInfor table tr:nth-child(5) td:nth-child(4) option:nth-child(5)')
    # 点选就诊类型为：无治疗
    jiuzhen_homepage1_button_button2_loc = (By.CSS_SELECTOR, 'html body #baseInfor table tr:nth-child(5) td:nth-child(6) input')
    #点选就诊类型为：门诊治疗
    jiuzhen_homepage1_button_button3_loc=(By.CSS_SELECTOR, 'html body #baseInfor table tr:nth-child(5) td:nth-child(6) input:nth-child(2)')
    # 点选就诊类型为：住院治疗
    jiuzhen_homepage1_button_button4_loc=(By.CSS_SELECTOR, 'html body #baseInfor table tr:nth-child(5) td:nth-child(6) input:nth-child(3)')
    #点选损失类型为：小额人伤
    jiuzhen_homepage1_button_small_loc = (By.CSS_SELECTOR, 'html body #baseInfor table tr:nth-child(5) td:nth-child(4) option:nth-child(2)')



#封装了一般损伤+无治疗的方法
    def yibanWu(self):
        self.actity3_window()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        logger.info('点选事故类型')
        self.click(*self.jiuzhen_homepage1_input_input1_loc)
        time.sleep(2)
        logger.info('点选损失类型为：一般损伤')
        self.click(*self.jiuzhen_homepage1_button_button1_loc)
        time.sleep(2)
        logger.info('点选就诊类型为：无治疗')
        self.click(*self.jiuzhen_homepage1_button_button2_loc)
        time.sleep(2)

#封装了一般损伤+门诊治疗的方法
    def yibanMen(self):
        self.actity3_window()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        logger.info('点选事故类型')
        self.click(*self.jiuzhen_homepage1_input_input1_loc)
        time.sleep(2)
        logger.info('点选损失类型为：一般损伤')
        self.click(*self.jiuzhen_homepage1_button_button1_loc)
        time.sleep(2)
        logger.info('点选就诊类型为：门诊治疗')
        # self.click(*self.jiuzhen_homepage1_button_button3_loc)
        # time.sleep(2)

#封装了一般损伤+住院治疗的方法
    def yibanZhu(self):
        self.actity3_window()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        logger.info('点选事故类型')
        self.click(*self.jiuzhen_homepage1_input_input1_loc)
        time.sleep(2)
        logger.info('点选损失类型为：一般损伤')
        self.click(*self.jiuzhen_homepage1_button_button1_loc)
        time.sleep(2)
        logger.info('点选就诊类型为：住院治疗')
        self.click(*self.jiuzhen_homepage1_button_button4_loc)
        time.sleep(2)

# 封装了伤残+门诊治疗的方法：
    def shangcanMen(self):
        self.actity3_window()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        logger.info('点选事故类型')
        self.click(*self.jiuzhen_homepage1_input_input1_loc)
        time.sleep(2)
        logger.info('点选损失类型为：伤残')
        self.click(*self.jiuzhen_homepage1_button_button5_loc)
        time.sleep(2)
        logger.info('点选就诊类型为：门诊治疗')
        self.click(*self.jiuzhen_homepage1_button_button3_loc)

#封装了伤残+住院治疗的方法：
    def shangcanZhu(self):
        self.actity3_window()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        logger.info('点选事故类型')
        self.click(*self.jiuzhen_homepage1_input_input1_loc)
        time.sleep(2)
        logger.info('点选损失类型为：伤残')
        self.click(*self.jiuzhen_homepage1_button_button5_loc)
        time.sleep(2)
        logger.info('点选就诊类型为：住院治疗')
        self.click(*self.jiuzhen_homepage1_button_button4_loc)

#封装了死亡+无治疗的方法：
    def siwangWu(self):
        self.actity3_window()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        logger.info('点选事故类型')
        self.click(*self.jiuzhen_homepage1_input_input1_loc)
        time.sleep(2)
        logger.info('点选损失类型为：死亡')
        self.click(*self.jiuzhen_homepage1_button_button6_loc)
        time.sleep(2)
        logger.info('点选就诊类型为：无治疗')
        self.click(*self.jiuzhen_homepage1_button_button2_loc)
        time.sleep(2)

#封装了死亡+门诊治疗的方法：
    def siwangMen(self):
        self.actity3_window()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        logger.info('点选事故类型')
        self.click(*self.jiuzhen_homepage1_input_input1_loc)
        time.sleep(2)
        logger.info('点选损失类型为：死亡')
        self.click(*self.jiuzhen_homepage1_button_button6_loc)
        time.sleep(2)
        logger.info('点选就诊类型为：门诊治疗')
        self.click(*self.jiuzhen_homepage1_button_button3_loc)
        time.sleep(2)

#封装了死亡+住院治疗的方法：
    def siwangZhu(self):
        self.actity3_window()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        logger.info('点选事故类型')
        self.click(*self.jiuzhen_homepage1_input_input1_loc)
        time.sleep(2)
        logger.info('点选损失类型为：死亡')
        self.click(*self.jiuzhen_homepage1_button_button6_loc)
        time.sleep(2)
        logger.info('点选就诊类型为：住院治疗')
        self.click(*self.jiuzhen_homepage1_button_button4_loc)
        time.sleep(2)



#封装了小额人伤+无治疗的方法
    def xiaoeWu(self):
        self.actity3_window()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        logger.info('点选事故类型')
        self.click(*self.jiuzhen_homepage1_input_input1_loc)
        time.sleep(2)
        logger.info('点选损失类型为：小额')
        self.click(*self.jiuzhen_homepage1_button_small_loc)
        time.sleep(2)

#封装了小额+门诊治疗的方法
    def xiaoeMen(self):
        self.actity3_window()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        logger.info('点选事故类型')
        self.click(*self.jiuzhen_homepage1_input_input1_loc)
        time.sleep(2)
        logger.info('点选损失类型为：小额人伤')
        self.click(*self.jiuzhen_homepage1_button_small_loc)
        time.sleep(2)
        logger.info('点选就诊类型为：门诊治疗')
        self.click(*self.jiuzhen_homepage1_button_button3_loc)

#封装了小额+住院治疗的方法
    def xiaoeZhu(self):
        self.actity3_window()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        logger.info('点选事故类型')
        self.click(*self.jiuzhen_homepage1_input_input1_loc)
        time.sleep(2)
        logger.info('点选损失类型为：小额人伤')
        self.click(*self.jiuzhen_homepage1_button_small_loc)
        time.sleep(2)
        logger.info('点选就诊类型为：住院治疗')
        self.click(*self.jiuzhen_homepage1_button_button4_loc)
















































