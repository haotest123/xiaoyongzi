from selenium import webdriver
import time

driver=webdriver.Chrome("../tools/chromedriver.exe")
try:
    driver.implicitly_wait(3)
    driver.get('http://127.0.0.1/upload/forum.php')
    driver_list = driver.current_window_handle  # 获取当前活跃的窗口
    driver.switch_to.window(driver_list)
    time.sleep(3)
    element = driver.find_element_by_css_selector('.y #ls_username')
    element.send_keys('admin')
    time.sleep(3)
    element1 = driver.find_element_by_css_selector('.y #ls_password')
    element1.send_keys('haotest')
    time.sleep(3)
    elements=driver.find_element_by_css_selector('.fastlg_l button')
    elements.click()
    time.sleep(3)


#进入默认板块，删除帖子
    # element2 = driver.find_element_by_css_selector('.bm_c table tr h2 a')
    #     # element2.click()
    #     # time.sleep(3)
    #     # element3=driver.find_element_by_css_selector('.o input')
    #     # element3.click()
    #     # time.sleep(3)
    #     # element4=driver.find_element_by_css_selector('#mdly p strong a')
    #     # element4.click()
    #     # time.sleep(3)
    #     # element5=driver.find_element_by_css_selector('.tm_c #moderateform .o button')
    #     # element5.click()
    #     # time.sleep(3)
#退出
    element11=driver.find_element_by_css_selector('.hdc #um p > *:last-child')
    element11.click()
    time.sleep(3)
    elementss = driver.find_element_by_css_selector('.y #ls_username')
    elementss.send_keys('admin')
    time.sleep(3)
    element12 = driver.find_element_by_css_selector('.y #ls_password')
    element12.send_keys('haotest')
    time.sleep(3)
    elements3=driver.find_element_by_css_selector('.fastlg_l button')
    elements3.click()
    time.sleep(3)
#进入版块管理（管理中心---论坛）
    element6=driver.find_element_by_css_selector('#um p:nth-child(2)>*:nth-last-child(3)')
    element6.click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)

    element7=driver.find_element_by_css_selector('#loginform .loginform input')
    element7.send_keys('haotest')
    time.sleep(3)
    element8=driver.find_element_by_css_selector('#loginform .loginnofloat input')
    element8.click()
    time.sleep(3)
    element9=driver.find_element_by_css_selector('#topmenu li:nth-of-type(7) em a')
    element9.click()
    time.sleep(3)

# 创建新的板块：
    driver.switch_to.frame('main')
    element10=driver.find_element_by_css_selector('.lastboard a')
    element10.click()
    time.sleep(3)
    # cpform > table > tbody:nth-child(3) > tr > td:nth-child(2) > div > a
    el13=driver.find_element_by_css_selector('tr:last-child td .board input')
    el13.send_keys('xiaoyongzi1')
    time.sleep(3)
    el=driver.find_element_by_css_selector('.fixsel .btn')
    el.click()
    time.sleep(3)
    driver.switch_to.default_content()
    time.sleep(3)

    el1=driver.find_element_by_css_selector('.uinfo p:first-child a')
    el1.click()
    time.sleep(3)

    el2=driver.find_element_by_css_selector('.hdc #um p > *:last-child')
    el2.click()

#登陆
    time.sleep(3)
    el3=driver.find_element_by_css_selector('.y #ls_username')
    el3.send_keys('anyong')
    time.sleep(3)
    el4=driver.find_element_by_css_selector('.y #ls_password')
    el4.send_keys('868686')
    time.sleep(3)
    el5=driver.find_element_by_css_selector('.fastlg_l .pn em')
    el5.click()
    time.sleep(3)
    el6=driver.find_element_by_css_selector('.fl_tb tbody>*:nth-last-child(2) td h2 a')
    el6.click()
# 发帖
    time.sleep(3)
    el7=driver.find_element_by_css_selector('.pbt .px')
    el7.send_keys('北京趣事')
    time.sleep(3)
    el8=driver.find_element_by_css_selector('.area #fastpostmessage')
    el8.send_keys('总是去各种地方看看！')
    time.sleep(3)
    el9=driver.find_element_by_css_selector('.ptm #fastpostsubmit')
    el9.click()
    time.sleep(3)
    el10=driver.find_element_by_css_selector('.pob em a')
    el10.click()
    time.sleep(3)
# 回帖
    el11=driver.find_element_by_css_selector('.area #postmessage')
    el11.send_keys('很好的想法')
    time.sleep(3)
    el12=driver.find_element_by_css_selector('.o .pn')
    el12.click()
    time.sleep(3)












finally:
    time.sleep(5)
    driver.quit()
