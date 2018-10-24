from selenium import webdriver
import time

#页面中有iframe嵌套
driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.implicitly_wait(5)
driver.get('https://mail.163.com/')
time.sleep(2)
driver.switch_to.frame('x-URS-iframe')
element=driver.find_element_by_name('email')
element.send_keys('adsad')
time.sleep(5)
driver.quit()