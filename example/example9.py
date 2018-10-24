from selenium import webdriver
import re

driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.implicitly_wait(5)#隐式等待
driver.get('http://home.baidu.com/home/index/contact_us')
print('联系百度已打开',driver.title)

doc = driver.page_source
email = re.findall(r'[\w]+@[\w\.-]+',doc)
print('数量：',len(email))
for i in email:
    print(i)



