from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
from framework.logger import Logger
from appium.webdriver.common.touch_action import TouchAction
import os.path
import time

logger=Logger(logger="BasePage").getlog()
class BasePage(object):
    # login_url='http://127.0.0.1/upload/forum.php'
    #初始化页面
    def __init__(self,driver):
        self.driver=driver
    def open_url(self,url):
        self.driver.get(url)

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info('找到页面元素', loc)
        except:
            logger.error('页面元素未找到%s', (self, loc))
#发生错误的截图处理
    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath('.'))+ '/screenshots/'
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        # 全路径
        screen_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('截得的图片保存在文件夹')
        except Exception as e:
            self.get_windows_img()
            logger.error('截图发生了错误%s',e)

    # 进行输入内容的方法
    def sendkeys(self, text, *loc):
        element = self.find_element(*loc)
        element.clear()
        try:
            element.send_keys(text)
            logger.info('输入框已找到%s', element.text)
        except:
            logger.error('页面输入框未找到%s', (self, loc))

    #点击元素
    def click(self,*loc):
        element=self.find_element(*loc)
        try:
            logger.info('元素已点击')
            element.click()
        except  Exception as e:
            logger.error('元素点击错误',e)

    #长按方法
    def TouchAction(self,*loc):
        el=self.driver.find_element(*loc)
        action1=TouchAction(self.driver)
        try:
            action1.press(el).wait(20000).perform()
            logger.info('长按正确')
        except:
            logger.info('长按错误')














