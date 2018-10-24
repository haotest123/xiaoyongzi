from selenium import webdriver
import time

driver=webdriver.Chrome("../tools/chromedriver.exe")
try:
    driver.implicitly_wait(3)
    driver.get('http://127.0.0.1/upload/forum.php')
    time.sleep(3)

    #普通用户登录：
    ele1=driver.find_element_by_css_selector('.y #ls_username')
    ele1.send_keys('anyong')
    time.sleep(3)
    ele2=driver.find_element_by_css_selector('.y #ls_password')
    ele2.send_keys('868686')
    time.sleep(3)
    ele3=driver.find_element_by_css_selector('.fastlg_l .pn em')
    ele3.click()
    time.sleep(3)
    ele4=driver.find_element_by_css_selector('.bm_c tbody tr td h2 a')
    ele4.click()
    time.sleep(3)

    # 点击发帖
    ele5=driver.find_element_by_css_selector('.mn >*:nth-child(3) #newspecial')
    ele5.click()
    time.sleep(3)
    #点击发起投票
    ele6=driver.find_element_by_css_selector('#ct div .tb li:last-child a')
    ele6.click()
    time.sleep(3)
    #输入标题
    ele7=driver.find_element_by_css_selector('#postbox .pbt .z span input')
    ele7.send_keys('天气状况')
    time.sleep(3)
    ele8=driver.find_element_by_css_selector('.exfm .sinf #pollm_c_1 p input')
    ele8.send_keys('晴天')
    time.sleep(3)
    ele9=driver.find_element_by_css_selector('.exfm .sinf #pollm_c_1 p:nth-child(2) input')
    ele9.send_keys('阴天')
    time.sleep(3)
    ele10=driver.find_element_by_css_selector('.exfm .sinf #pollm_c_1 p:nth-child(3) input')
    ele10.send_keys('雨天')
    time.sleep(3)

    #点击发起投票
    elem1=driver.find_element_by_css_selector('.mtm button')
    elem1.click()
    time.sleep(3)
    #点击单选投票按钮
    elem2=driver.find_element_by_css_selector('.pslt input')
    elem2.click()
    time.sleep(3)
    #点击提交按钮
    elem3=driver.find_element_by_css_selector('.pcht tbody tr:last-child button')
    elem3.click()
    time.sleep(3)
    elem4=driver.find_element_by_css_selector('#postlist > table:nth-child(1) > tbody > tr > td.plc.ptm.pbn.vwthd > h1 span')


#.pcht tbody tr .pvt label
#.pcht tbody tr:nth-child(2) td:last-child
finally:
    time.sleep(3)
    driver.quit()