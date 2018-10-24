from selenium import webdriver

driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.get('http://www.baidu.com')
assert '百度一下,你就知道' in driver.title