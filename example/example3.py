import time
from selenium import webdriver

driver=webdriver.Chrome("../tools/chromedriver.exe")
#上一个代码执行完，等待5秒执行下一个代码
driver.implicitly_wait(5)
driver.get('http://www.baidu.com')
#激活当前窗口
driver.switch_to.window(driver.current_window_handle)
#控制台输出信息
print('百度首页已打开',driver.title)

#查找搜索框，通过属性id
search_input=driver.find_element_by_id('kw')
#找到后，输入值并提交搜索
search_input.send_keys('胡歌')
search_input.submit()
#获取页面中“百度为您找到相关结果约15,100,000个”相关文字的元素
nums=driver.find_element_by_class_name('nums')
print(nums.text)
#再次激活窗口
driver.switch_to.window(driver.current_window_handle)
#执行脚本，显示一个框提示用户
a=10
driver.execute_script("window.alert(\"{},{}秒后关闭\")".format(nums.text.replace("\n","\t"),a))
time.sleep(10)
