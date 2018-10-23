from appium import webdriver
from framework.logger import Logger
from configparser import ConfigParser
import os.path

logger=Logger(logger='AppEngine').getlog()
class AppEngine(object):
    dir_path = os.path.dirname(os.path.abspath('.'))

    def open_app(self):
        config=ConfigParser()
        apk_path=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'

        #读取文件
        config.read(apk_path)

        desired_caps={}
        desired_caps['platformName']=config.get('appType',['platformName'])
        logger.info('设备系统%s',desired_caps['platformName'])

        desired_caps['platformVersion']= config.get('appType', ['platformVersion'])
        logger.info('设备版本号%s', desired_caps['platformVersion'])

        desired_caps['deviceName']= config.get('appType', ['deviceName'])
        logger.info('设备版本号%s', desired_caps['platformVersion'])

        desired_caps['appPackage']= config.get('testServer', ['appPackage'])
        logger.info('   设备名称%s', desired_caps['appPackage'])

        desired_caps['appActivity']= config.get('testServer', ['appActivity'])

        desired_caps['sessionOverride']= config.get('testServer', ['sessionOverride'])

        desired_caps['noRest']= config.get('testServer', ['noRest'])

        if  desired_caps=='Android':
            driver=webdriver.Remote(self.dir_path)

        driver.implicitly_wait(5)
    def quit_app(self):
        self.driver.quit()

































