from selenium.webdriver.common.by import By
from PageObjects.base import BasePage
from framework.logger import Logger
import time


#获取一个loger对象，调用getlog()方法:
logger=Logger(logger="zhenduan_homepage").getlog()


#封装了添加诊断伤情页面的方法：
class zhenduan_homepage(BasePage):
    ##点选第一个诊断伤情---关键字查询
    zhenduan_homepage_button_button1_loc=(By.CSS_SELECTOR,'html body tbody tr:nth-child(2) .textfield')#点击输入框
    zhenduan_homepage_input_input_loc=(By.CSS_SELECTOR,'html body tbody tr:nth-child(2) .textfield')#输入伤情名称
    # 点击查询
    zhenduan_homepage_button_button2_loc=(By.CSS_SELECTOR,'html body tbody tr:nth-child(2) td:last-child input')

    #点选第一个诊断伤情---关键字查询
    zhenduan_homepage_button_button3_loc=(By.CSS_SELECTOR,'html body div .data-show tbody .tb_tr td')
    # 点选第一个诊断伤情---点选左侧树
    zhenduan_homepage_button_button6_loc=(By.CSS_SELECTOR,'html body #treeMain #tree_1_switch')#伤情分类
    zhenduan_homepage_button_button7_loc=(By.CSS_SELECTOR,'html body #treeMain #tree_1_ul #tree_2_switch')#头部
    zhenduan_homepage_button_button8_loc=(By.CSS_SELECTOR,'html body #treeMain #tree_1_ul #tree_2_ul #tree_15_span')#头皮
    #点选第一个诊断伤情--图新分类
    zhenduan_homepage_button_button9_loc=(By.CSS_SELECTOR,'html body .tab-query tr:last-child td:last-child input:nth-child(2)')#图形分类
    zhenduan_homepage_button_button10_loc=(By.CSS_SELECTOR,'html body .mian #body_map area')#头部图形


    # 点击添加到已选择
    zhenduan_homepage_button_button4_loc=(By.CSS_SELECTOR,'html body .data .button')
    #点击添加到主页面
    zhenduan_homepage_button_button5_loc=(By.CSS_SELECTOR,'html body .data .button')

# 封装的第三个添加诊断伤情的方法：点选第一个诊断伤情---左侧树查询
    def shangqing2(self):
        self.actity1_window()  # 激活当前窗口
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('topFrame')
        logger.info('点击图形分类')
        self.click(*self.zhenduan_homepage_button_button9_loc)
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('leftCmitFrame')
        time.sleep(2)
        logger.info('点击头部图形')
        self.click(*self.zhenduan_homepage_button_button10_loc)
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('rightCmitFrame')
        time.sleep(2)
        logger.info('点选第一个伤情')
        self.click(*self.zhenduan_homepage_button_button3_loc)
        time.sleep(2)
        logger.info('点击添加到已选择')
        self.click(*self.zhenduan_homepage_button_button4_loc)
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('bottomCmitFrame')
        logger.info('点击添加到主页面')
        self.click(*self.zhenduan_homepage_button_button5_loc)
        time.sleep(2)

# 封装的第一个添加诊断伤情的方法：点选第一个诊断伤情---关键字查询
    def shangqing(self, sqname):
        self.actity1_window()  # 激活当前窗口
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('topFrame')
        logger.info('输入伤情名称')
        self.click(*self.zhenduan_homepage_button_button1_loc)
        time.sleep(2)
        self.sendkeys(sqname, *self.zhenduan_homepage_input_input_loc)
        time.sleep(2)
        logger.info('点击查询按钮')
        self.click(*self.zhenduan_homepage_button_button2_loc)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('rightCmitFrame')
        time.sleep(2)
        logger.info('点选第一个伤情')
        self.click(*self.zhenduan_homepage_button_button3_loc)
        time.sleep(2)
        logger.info('点击添加到已选择')
        self.click(*self.zhenduan_homepage_button_button4_loc)
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('bottomCmitFrame')
        logger.info('点击添加到主页面')
        self.click(*self.zhenduan_homepage_button_button5_loc)
        time.sleep(2)

# 封装的第二个添加诊断伤情的方法：点选第一个诊断伤情---点选图新分类
    def shangqing1(self):
        self.actity1_window()  # 激活当前窗口
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('leftCmitFrame')
        logger.info('点击伤情分类')
        self.click(*self.zhenduan_homepage_button_button6_loc)
        time.sleep(2)
        logger.info('点击头部')
        self.click(*self.zhenduan_homepage_button_button7_loc)
        time.sleep(2)
        logger.info('点击头皮')
        self.click(*self.zhenduan_homepage_button_button8_loc)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('rightCmitFrame')
        time.sleep(2)
        logger.info('点选第一个伤情')
        self.click(*self.zhenduan_homepage_button_button3_loc)
        time.sleep(2)
        logger.info('点击添加到已选择')
        self.click(*self.zhenduan_homepage_button_button4_loc)
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('bottomCmitFrame')
        logger.info('点击添加到主页面')
        self.click(*self.zhenduan_homepage_button_button5_loc)
        time.sleep(2)






















        # js = 'document.getElementsByClassName("prefpanelgo")[0].click()'
        # self.driver.execute_script(js)
        # # # 判断alert弹出框
        # # result = EC.alert_is_present()(self.driver)
        # # if result:
        # #     result.accept()
        # # else:
        # #     self.driver.quit()































