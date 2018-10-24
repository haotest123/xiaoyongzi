from selenium import webdriver

#创建一个新的chrome浏览器
driver=webdriver.Chrome("../tools/chromedriver.exe")
#在给定的网址进入此网址页面
driver.get("http://www.python.org")
#判断Python是否在当前浏览器的title中
assert "Python" in driver.title
