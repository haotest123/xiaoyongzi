from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.implicitly_wait(5)
driver.get('https://www.python.org/')
time.sleep(3)
menu=driver.find_element_by_css_selector('.navigation #downloads')
time.sleep(3)
hidden_submenu=driver.find_element_by_css_selector('.navigation #downloads .subnav .tier-2')
ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()
