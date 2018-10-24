from selenium import webdriver

driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.get('http://www.baidu.com')
print('百度首页已打开',driver.title)

s=driver.find_elements_by_tag_name('a')
print('数量:',len(s))
for link in s:
    #print(link.get_attribute("href"))
    print(link.text)



