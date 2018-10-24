import time
from selenium import webdriver
driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.implicitly_wait(5)
driver.get('http://www.baidu.com')
print('百度首页已打开',driver.title)

search_input=driver.find_element_by_id('kw')
search_input.send_keys('胡歌')
search_input.submit()
nums=driver.find_element_by_class_name('nums')
print(nums.text)
wait_seconds=10
driver.execute_script('window.alert(\'{},{}秒后关闭\')'.format(nums.text.replace('\n','\t'),wait_seconds))
time.sleep(10)
driver.quit()