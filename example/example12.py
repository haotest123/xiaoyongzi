from selenium import webdriver
import time

#弹出框
driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.implicitly_wait(5)
driver.get('https://www.baidu.com/')
time.sleep(3)
driver.execute_script('window.alert("你好，世界")')
time.sleep(3)
#driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()
time.sleep(3)
driver.quit()