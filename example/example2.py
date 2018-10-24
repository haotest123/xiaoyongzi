from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  time

#打开一个chrome浏览器-
driver=webdriver.Chrome("../tools/chromedriver.exe")
#打开某一个页面
driver.get("http://www.yahoo.com")
assert "Yahoo" in driver.title
#通过name找到文本输入框，
element=driver.find_element_by_name('p')
#在文本框中输入内容，并回车搜索
element.send_keys('seleniumhq'+Keys.RETURN)
time.sleep(5)
driver.quit()

