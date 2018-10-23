from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import os

apk_path=os.path.dirname(os.path.abspath('.'))

desired_caps={}
desired_caps['platformName']='Android'  #设备系统
desired_caps['platformVersion']='6.0.1'  #设备版本号
desired_caps['deviceName']='127.0.0.1:21503' #设备名称
# 覆盖session信息，可多次建立session会话
desired_caps['sessionOverride']=True
# 测试apk包的路径
desired_caps['app']=apk_path + '/app/todolist.apk'
#应用程序的包名
desired_caps['appPackage']='com.example.todolist'
#激活app界面
desired_caps['appActivity']='com.example.todolist.LoginActivity'
#不需要每次都安装apk
desired_caps['noRest']=True
#启动app
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

# driver1=driver.find_element_by_id('com.example.todolist:id/nameET').send_keys('1')
# driver2=driver.find_element_by_id('com.example.todolist:id/passwordET').send_keys('1')
# driver3=driver.find_element_by_id('com.example.todolist:id/loginBtn').click()
# 登录
driver1=driver.find_element_by_class_name('android.widget.EditText').send_keys('1')
driver2=driver.find_element_by_id('com.example.todolist:id/passwordET').send_keys('1')
driver3=driver.find_element_by_class_name('android.widget.Button').click()
#点击+号新建
driver4=driver.find_element_by_id('com.example.todolist:id/action_new').click()
#新建内容
driver5=driver.find_element_by_id('com.example.todolist:id/toDoItemDetailET').send_keys('aaaaa')
#点击保存
driver6=driver.find_element_by_class_name('android.widget.Button').click()
#退出
# drivers=driver.find_element_by_class_name('android.widget.ImageButton').click()
# drivers1=driver.find_element_by_class_name('android.widget.LinearLayout').click()
# drivers2=driver.find_element_by_id('android:id/button1').click()
#长按找到删除
# el = driver.find_element_by_class_name('android.widget.RelativeLayout')
# elx=el.location.get('x')
# ely=el.location.get('y')
# driver.swipe(77,116,1203,176,20000)
el =driver.find_element_by_xpath('//android.widget.ListView/android.widget.RelativeLayout')
action1=TouchAction(driver)
action1.long_press(el).wait(20000).perform()

#点击删除
driver14=driver.find_element_by_xpath('//android.widget.ListView/android.widget.LinearLayout[2]').click()
#点击确定
driver15=driver.find_element_by_id('android:id/button1').click()



# driver1=driver.find_element_by_xpath('//android.widget.EditText[@test="输入用户名"]').send_keys('1')
# driver2=driver.find_element_by_xpath('//android.widget.EditText[@test="输入密码"]').send_keys('1')
# driver3=driver.find_element_by_xpath('//android.widget.Button').click()















# apk_path = os.path.dirname(os.path.abspath('.'))
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '6.0.1'
# desired_caps['deviceName'] = '127.0.0.1:21503'     # 设备名称
# desired_caps['sessionOverride'] =True
#
# desired_caps['app'] = apk_path + '/app/todolist.apk'
#
# desired_caps['noReset'] = True
#
# desired_caps['appPackage'] = 'com.example.todolist'
# desired_caps['appActivity'] = 'com.example.todolist.LoginActivity'
#
# driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)