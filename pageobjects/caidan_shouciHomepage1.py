from PageObjects.base import BasePage
from framework.logger import Logger
from selenium.webdriver.common.by import By
import time
#获取一个loger对象，调用getlog()方法:
logger=Logger(logger="shouci_homepage1").getlog()

class shouci_homepage1(BasePage):
#点击首次查勘------处理任务
    shouci_homepage1_button_click1_loc=(By.CLASS_NAME,'level2-node')
    #选择任务类型：待处理
    shouci_homepage1_select_click2_loc=(By.CSS_SELECTOR,'html body .query tr td:nth-child(4) option:nth-child(2)')
    #点击查询按钮
    shouci_homepage1_button_click3_loc=(By.CSS_SELECTOR,'html body .query tr:last-child td:last-child .button')
    # #点击报案号进入(此方法已封装在base文件的有无手机图标方法中)
    # shouci_homepage1_button_click4_loc=(By.CSS_SELECTOR,'html body .data .data-show tbody tr td a')

#跟踪审核
    #首次查勘提交后，在页面中点击 处理案件 按钮
    genzong_homepage1_button_button1_loc=(By.CSS_SELECTOR,'html body .info_region td:nth-child(2) input:nth-child(2)')
    #点选下一环节---跟踪审核
    genzong_homepage1_button_button2_loc=(By.CSS_SELECTOR,'html body div:nth-child(24) table tr:nth-child(3) td:nth-child(2) option:nth-child(2)')
    #输入跟踪记录
    genzong_homepage1_button_input1_loc=(By.CSS_SELECTOR,'html body div:nth-child(24) table tr:nth-child(6) .textfield')
    #点击提交按钮
    genzong_homepage1_button_button3_loc=(By.CSS_SELECTOR,'html body .floatDiv div:nth-child(2) input:nth-child(3)')
    #点击确定按钮
    genzong_homepage1_button_button4_loc=(By.CSS_SELECTOR,'html body .layui-layer-btn a')


#小额人伤
    #点击小额人伤
    xiaoe_homepage1_div_click_loc = (By.CSS_SELECTOR, 'html body .level1:nth-child(3)')
    #点击小额人伤-处理任务
    xiaoe_homepage1_div_click1_loc = (By.CSS_SELECTOR, 'html body div:nth-child(3) div:last-child div:last-child')
    #选择伤者姓名
    xiaoe_homepage1_selec_loc=(By.CSS_SELECTOR,'html body .query table tbody tr:first-child td:first-child option:nth-child(6)')
    #录入伤者姓名：小额住院自动化
    xiaoe_homepage1_input_szName_loc=(By.CSS_SELECTOR,'html body .query table tbody tr:first-child td:nth-child(2) .textfield')


    def shouci(self):
        logger.info('点击首次查勘------处理任务')
        self.driver.switch_to.frame('leftFrame')
        self.click(*self.shouci_homepage1_button_click1_loc)
        time.sleep(2)
        logger.info('点选待处理')
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        self.click(*self.shouci_homepage1_select_click2_loc)
        time.sleep(2)
        logger.info('点击查询')
        self.click(*self.shouci_homepage1_button_click3_loc)
        logger.info('点击报案号')
        self.phone_icon()
    def genzong(self,jilu):
        logger.info('点击处理案件按钮')
        self.click(*self.genzong_homepage1_button_button1_loc)
        time.sleep(2)
        self.actity_window()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        time.sleep(2)
        logger.info('点选下一环节：跟踪审核')
        self.click(*self.genzong_homepage1_button_button2_loc)
        time.sleep(2)
        logger.info('输入跟踪记录')
        self.sendkeys(jilu,*self.genzong_homepage1_button_input1_loc)
        time.sleep(2)
        logger.info('点击提交按钮')
        self.click(*self.genzong_homepage1_button_button3_loc)
        time.sleep(2)
        logger.info('点击确定按钮')
        self.click(*self.genzong_homepage1_button_button4_loc)
        time.sleep(2)

    def xiaoe(self,szName):
        logger.info('点击小额人伤')
        self.driver.switch_to.frame('leftFrame')
        self.click(*self.xiaoe_homepage1_div_click_loc)
        time.sleep(2)
        logger.info('点击处理任务')
        self.click(*self.xiaoe_homepage1_div_click1_loc)
        time.sleep(2)
        logger.info('选择伤者姓名')
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        self.click(*self.xiaoe_homepage1_selec_loc)
        time.sleep(2)
        logger.info('录入伤者姓名')
        self.sendkeys(szName, *self.xiaoe_homepage1_input_szName_loc)
        time.sleep(2)
        logger.info('点击查询')
        self.click(*self.shouci_homepage1_button_click3_loc)
        logger.info('点击报案号')
        self.phone_icon()
























