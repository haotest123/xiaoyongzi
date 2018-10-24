from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome('./chromedriver.exe')
try:
    driver.implicitly_wait(5) #隐式等待
    driver.get('https://www.lagou.com/zhaopin/Java/?=labelWords=lable')
    driver_list=driver.current_window_handle#获取当前活跃的窗口
    driver.switch_to.window(driver_list)
    while True:
        jobs = driver.find_elements_by_css_selector('.item_con_list li')
        for job in jobs:
            job_link = job.find_element_by_css_selector('.p_top a span')
            # job_link=driver.find_element_by_css_selector('.item_con_list li:first-child .p_top a span')
            job_link.click()

            driver.switch_to.window(driver.window_handles[1])  # 切换到第二个窗口
            job_company = driver.find_element_by_css_selector('.company')
            job_name = driver.find_element_by_css_selector('.name')
            job_money = driver.find_element_by_css_selector('.salary')
            print('公司名称:', job_company.text, '职位名称:', job_name.text, '资金:', job_money.text)
            driver.close()
            driver.switch_to.window(driver_list)
        next_page = WebDriverWait(driver, 5).until(ec.element_to_be_clickable(
            (By.CSS_SELECTOR, '.s_position_list .item_con_pager .pager_container > *:last-child')))
        next_page_class = next_page.get_attribute('class')
        if 'pager_next_disabled' in next_page_class:
            break
        else:
            next_page.click()
            time.sleep(3)

finally:
    time.sleep(5)
    driver.quit()