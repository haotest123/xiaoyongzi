from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome("../tools/chromedriver.exe")
driver.implicitly_wait(5)
driver.get('https://www.baidu.com')
driver.switch_to.window(driver.current_window_handle)
try:
    #显示等待
    element=WebDriverWait(driver,5).until(ec.element_to_be_clickable((By.CSS_SELECTOR,'.mnav')))

    element.click()
    print(driver.title)
finally:
    time.sleep(5)
    #driver.quit()