from selenium import webdriver

driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.implicitly_wait(5)
driver.get('http://home.baidu.com/home/index/contact_us')
print('联系百度已打开',driver.title)
email=driver.find_elements_by_class_name('mail-content-text')
str='@baidu.com'
for link in email:
    if str in link.text:
        print(link.text)


