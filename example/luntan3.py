from selenium import webdriver
import time

driver=webdriver.Chrome("../tools/chromedriver.exe")
try:
    driver.implicitly_wait(3)
    driver.get('http://127.0.0.1/upload/forum.php')
    driver_list = driver.current_window_handle  # 获取当前活跃的窗口
    driver.switch_to.window(driver_list)
    time.sleep(5)
    #用户登录
    element = driver.find_element_by_css_selector('.y #ls_username')
    element.send_keys('anyong')
    time.sleep(3)
    element1 = driver.find_element_by_css_selector('.y #ls_password')
    element1.send_keys('868686')
    time.sleep(3)
    element2 = driver.find_element_by_css_selector('.fastlg_l .pn em')
    element2.click()
    time.sleep(3)

    #进行帖子搜索
    element3=driver.find_element_by_css_selector('.scbar_txt_td .xg1')
    element3.send_keys('haotest')
    time.sleep(3)
    element4=driver.find_element_by_css_selector('.scbar_btn_td .pn')
    element4.click()
    time.sleep(3)
    #进入搜索的帖子
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    element5=driver.find_element_by_css_selector('.pbw .xs3 a')
    element5.click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(3)
    assert 'haotest' in driver.title

    if 'haotest' in driver.title:
        print('标题正确')
    else:
        print('标题错误')

    # um > p:nth-child(2) > a:nth-child(13)


finally:
    time.sleep(5)
    driver.quit()