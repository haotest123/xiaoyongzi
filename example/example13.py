from selenium import webdriver
import time

#滚动条
driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.implicitly_wait(5)
driver.get('http://bbs.tianya.cn//')
time.sleep(5)
driver.execute_script("document.getElementById('bbs_left_nav').scrollTop=500")
time.sleep(5)
driver.quit()