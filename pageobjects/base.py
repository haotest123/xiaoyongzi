from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
from framework.logger import Logger
import os.path
import time

#获取一个loger对象，调用getlog()方法:
logger=Logger(logger="BasePage").getlog()

class BasePage(object):
    # login_url='http://127.0.0.1/upload/forum.php'
    #初始化页面
    def __init__(self,driver):
        self.driver=driver

     # 浏览器打开一个页面
    def open_url(self,url):
        self.driver.get(url)
        #浏览器关闭并推出
    # def quit_browser(self):
    #     self.driver.quit()
    def close(self):
        try:
            self.driver.close()
            logger.info('关闭并退出浏览器')
        except Exception as e:
            logger.error('退出浏览器发生错误%s',e)
     #一个*是元组，两个*是字典
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info('找到页面元素',loc)
        except:
            logger.error('页面元素未找到%s',(self,loc))
    #保存图片
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
    #进行输入内容
    def sendkeys(self,text,*loc):
        element=self.find_element(*loc)
        element.clear()
        try:
            element.send_keys(text)
            logger.info('输入框已找到%s',element.text)

        except:
            logger.error('页面输入框未找到%s',(self,loc))
    #清除文本框:
    def clear(self,*loc):
        element=self.find_element(*loc)
        #element.clear()
        try:
            element.clear()
        except:
            logger.erron('清除元素未找到%s', (self, loc))
    #点击元素
    def click(self,*loc):
        element=self.find_element(*loc)
        try:
            logger.info('元素已点击')
            element.click()
        except  Exception as e:
            logger.error('元素点击错误',e)
#窗口切换
    def actity_window(self):
        try:
            self.driver.switch_to.window(self.driver.current_window_handle)
            logger.info('激活当前窗口')
        except:
            logger.error('激活窗口失败')
    def actity1_window(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            logger.info('激活当前窗口')
        except:
            logger.error('激活窗口失败')
    def actity2_window(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[2])
            logger.info('激活当前窗口')
        except:
            logger.error('激活窗口失败')
#iframe嵌套
    def in_moudle(self,content):
        try:
            self.driver.switch_to.frame(content)
            logger.info('进入iframe模块正确')
        except:
            logger.error('进入iframe模块错误')
    def quit_moudle(self):
        try:
            self.driver.switch_to.default_content()
            logger.info('跳出iframe模块正确')
        except:
            logger.error('跳出iframe模块错误')
    def element_in_title(self,content,*loc):
        self.content = self.find_element(*loc)
        try:
            assert content in self.driver.title
            logger.info('标题正确')
        except:
            logger.error('标题错误')

# 投票选取方法
    def element_output_title(self,*loc):
        element= self.find_element(*loc)
        try:

            logger.info('The element %s was print' %element.text)
        except:
            logger.error('元素没有选取成功')














