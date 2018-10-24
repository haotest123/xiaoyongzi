from selenium import webdriver
from framework.logger import Logger
from configparser import ConfigParser
import os.path

logger=Logger(logger='BrowserEngine').getlog()

class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath('.'))
    chrome_driver_path=dir+'/tools/chromedriver.exe'

    def open_browser(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        # 读文件
        config.read(file_path)

        browser=config.get('browserType','browserName')
        logger.info('你选择的浏览器是:%s',browser)
        url=config.get('testServer','URL')
        logger.info('要进行测试的网址:%s',url)
        if browser=='Chrome':
            driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info('启动了Chrome浏览器')
        driver.get(url)
        logger.info('打开网址:%s',url)
        driver.maximize_window()
        logger.info('窗口最大化')
        driver.implicitly_wait(5)
        logger.info('隐式等待5秒')
        return driver

    def quit_browser(self):
        self.driver.quit()
        logger.info('关闭并停止浏览器')