from appium import webdriver
import unittest
from framework.app_engine import AppEngine

class Base_testcase(unittest.TestCase):
    def setUp(self):
        app=AppEngine()
        self.driver=app.open_app()

        # apk_path = os.path.dirname(os.path.abspath('.'))
        # desired_caps = {}
        # desired_caps['platformName'] = 'Android'  #设备系统
        # desired_caps['platformVersion'] = '6.0.1'  #设备版本号
        # desired_caps['deviceName'] = '127.0.0.1:21503'  #设备名称
        # # 应用程序的包名
        # desired_caps['appPackage'] = 'com.example.todolist'
        # # 激活app界面
        # desired_caps['appActivity'] = 'com.example.todolist.LoginActivity'
        # # 覆盖session信息，可多次建立session会话
        # desired_caps['sessionOverride'] = True
        # # 测试apk包的路径
        # desired_caps['app'] = apk_path + '/app/todolist.apk'
        # # 不需要每次都安装apk,只是启动app
        # desired_caps['noRest'] = True
        # # 启动app
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def tearDown(self):
        self.driver.quit()
