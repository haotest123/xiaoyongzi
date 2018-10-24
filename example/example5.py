from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.get('http://www.baidu.com')
assert '百度一下，你就知道' in driver.title
element=driver.find_element_by_name('wd')
element.send_keys('胡歌'+ Keys.RETURN)
#driver.quit()