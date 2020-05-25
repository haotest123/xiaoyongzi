from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver import ActionChains
import time
import random
from selenium.webdriver.support import expected_conditions as EC
import re
import random
from datetime import timedelta, date
id_code_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
check_code_list = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
class IDcard:
    def gen_id_card(area_code, age, gender):
        datestring = str(date(date.today().year - age, 1, 1) + timedelta(days=random.randint(0, 364))).replace("-", "")
        rd = random.randint(0, 999)
        if gender == 0:
            gender_num = rd if rd % 2 == 0 else rd + 1
        else:
            gender_num = rd if rd % 2 == 1 else rd - 1
        result = str(area_code) + datestring + str(gender_num).zfill(3)
        return result + str(check_code_list[sum([a * b for a, b in zip(id_code_list, [int(a) for a in result])]) % 11])
    if __name__ == "__main__":
        area_code = random.choice(["420102", "420103", "420104", "420105", "420106", "420107"])
        id_number = gen_id_card(int(area_code), 22, 1)
driver=webdriver.Chrome("./tools/chromedriver.exe")
# driver=webdriver.Firefox()
#在给定的网址进入此网址页面
driver.get("https://testmcmscloud.iclaim.cn:6443/mcms2/?username=211000001&password=FA246D0262C3925617B0C72BB20EEB1D&loginValidateCode=B59C67BF196A4758191E42F76670CEBA&clientId=93DD4DE5CDDBA2C733C65F233097F05A")
driver.maximize_window()
driver_list=driver.current_window_handle#获取当前活跃的窗口
time.sleep(2)
#点击首次查勘------处理任务
driver.switch_to.frame('leftFrame')
chuli=driver.find_element_by_class_name('level2-node')
chuli.click()
time.sleep(2)
#选择任务类型：待处理
driver.switch_to.default_content()
driver.switch_to.frame('mainFrame')
renwu=driver.find_element_by_css_selector('html body .query tr td:nth-child(4) option:nth-child(2)')
renwu.click()
time.sleep(2)
#点击查询按钮
chaxun=driver.find_element_by_css_selector('html body .query tr:last-child td:last-child .button')
chaxun.click()
time.sleep(2)

#
# #**************************************************************
# # baoan = driver.find_element_by_css_selector('html body .data .data-show tbody tr td a')
# # time.sleep(2)
# # baoan.click()
# # time.sleep(2)
# # aler = driver.switch_to_alert()
# # time.sleep(2)
# # aler.accept()
# # baoan2 = driver.find_element_by_css_selector('html body .data .data-show tbody tr td a')
# # baoan2.click()
# # time.sleep(2)
# #*******************************************************************
# def public():
#     # anhao=driver.find_element_by_css_selector('html body .data .data-show tbody tr:nth-child(4) td a')
#     anhao = driver.find_element_by_css_selector('html body .data .data-show tbody tr:nth-child(9)')
#     anhao.click()
#     time.sleep(2)
# def ru():
#     # baoan =driver.find_element_by_css_selector('html body .data .data-show tbody tr td a')
#     # baoan.click()
#     # time.sleep(2)
#     public()
#     aler = driver.switch_to_alert()
#     time.sleep(2)
#     aler.accept()
#     time.sleep(2)
#     public()
# # def run1():
# #     baoan2 =driver.find_element_by_css_selector('html body .data .data-show tbody tr td a')
# #     baoan2.click()
# #     time.sleep(2)
# hang=driver.find_elements_by_css_selector('html body .data .data-show tbody tr:nth-child(9)')
# a=[hang]
# img=driver.find_element_by_xpath('//html//body//div[2][@class]//table[2][@id="data-list"]//tbody//tr//a')
# # img1= driver.find_elements_by_css_selector('html body .data .data-show tbody tr:nth-child(9) td:nth-child(7) img')
# # img2=driver.find_element_by_css_selector('html body .data .data-show tbody tr td:nth-child(7)')


#
# #**********************************************************************************

#点击报案号进入
# baoan1=driver.find_element_by_css_selector('html body .data .data-show tbody tr td a')
baoan1=driver.find_element_by_xpath('//html//body//div[2][@class]//table[2][@id="data-list"]//tbody//tr//a')
baoan1.click()
time.sleep(2)
#输入事故类型、损失类型、就诊类型：
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame('mainFrame')
shigu=driver.find_element_by_css_selector('html body #baseInfor table tr:nth-child(5) td:nth-child(2) option:nth-child(2)')
shigu.click()
time.sleep(2)
#损失类型
sunshi=driver.find_element_by_css_selector('html body #baseInfor table tr:nth-child(5) td:nth-child(4) option:nth-child(3)')
sunshi.click()
time.sleep(2)
#就诊类型
jiuzhen=driver.find_element_by_css_selector('html body #baseInfor table tr:nth-child(5) td:nth-child(6) input')
jiuzhen.click()
time.sleep(2)
#输入伤者姓名、联系电话,点选伤者类型
sznamae=driver.find_element_by_css_selector('html body #baseInfor table tr:nth-child(6) td:nth-child(2) .textfield')
sznamae.clear()
time.sleep(2)
sznamae.send_keys('自动化')
time.sleep(2)
phone=driver.find_element_by_css_selector('html body #baseInfor table tr:nth-child(6) td:nth-child(4) .textfield')
phone.clear()
time.sleep(2)
phone.send_keys('88888888')
time.sleep(2)
#点选伤者类型
rs=driver.find_element_by_css_selector('html body #baseInfor table tr:nth-child(7) td:nth-child(2) input')
rs.click()
time.sleep(2)
#输入身份证号：
ID=driver.find_element_by_css_selector('html body #doLoadFSurvey .info_region table tr:nth-child(8) td:nth-child(4) input')
ID.clear()
time.sleep(2)
area_code = random.choice(["420102", "420103", "420104", "420105", "420106", "420107"])
IDc=IDcard.gen_id_card(area_code,22,1)
ID.send_keys(IDc)
time.sleep(2)
#事故责任比例
zeren=driver.find_element_by_css_selector('html body #baseInfor table tr:nth-child(10) td:nth-child(2) .textfield option:nth-child(3)')
zeren.click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,400)", "")
time.sleep(2)


#点选户口性质
xingzhi=driver.find_element_by_css_selector('html body #referenceStandardDiv table tr td:last-child option:nth-child(2)').click()
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()
time.sleep(2)







# #点击增加医院
# yiyuan=driver.find_element_by_css_selector('html body #doLoadFSurvey #hospitalDIV div .other .button').click()
# time.sleep(2)
# #点击增加医院图标
# yiyuan1=driver.find_element_by_css_selector('html body #doLoadFSurvey #hospitalDIV .tab-query tr td:nth-child(2) img').click()
# time.sleep(2)
# driver.switch_to.frame('layui-layer-iframe1')
# time.sleep(2)
# #点击医院
# yiyuan2=driver.find_element_by_css_selector('html .body .data-show tr td a').click()
# time.sleep(2)
#
# driver.switch_to.default_content()
# driver.switch_to.frame('mainFrame')
# #点选门诊/住院日期
# da=driver.find_element_by_css_selector('html body #doLoadFSurvey #hospitalDIV .tab-query tr td:nth-child(4) #in').click()
# time.sleep(2)
# #点选日期
# driver.switch_to.frame(1)#用frame的index来定位，第一个是0
# time.sleep(2)
# data1=driver.find_element_by_css_selector('html body div #dpControl #dpTodayInput').click()
# time.sleep(2)
# driver.switch_to.default_content()
# driver.switch_to.frame('mainFrame')


#点击添加诊断
# driver.execute_script("window.scrollBy(0,200)", "")
# time.sleep(2)
tianjia=driver.find_element_by_css_selector('html body #doLoadFSurvey #diagnosisDIV .titleInfo .other .button')
# driver.execute_script("$(arguments[0]).click()",tianjia) #调用js进行点击元素
tianjia.click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])  # 切换到第二个窗口
time.sleep(2)
# 输入伤情名称，点击查询
driver.switch_to.default_content()
driver.switch_to.frame('topFrame')
time.sleep(2)
driver.find_element_by_css_selector("html body tbody tr:nth-child(2) .textfield").click()
time.sleep(2)
shangqing=driver.find_element_by_css_selector('html body tbody tr:nth-child(2) .textfield')
shangqing.send_keys('擦伤')
time.sleep(2)
chaxun2=driver.find_element_by_css_selector('html body tbody tr:nth-child(2) td:last-child input')
chaxun2.click()
time.sleep(2)
# driver.switch_to.default_content()
# driver.switch_to.frame('topFrame')
# tuxing=driver.find_element_by_css_selector('html body .tab-query tr:last-child td:last-child input:nth-child(2)')
# tuxing.click()
# time.sleep(2)
# toubu=driver.find_elements_by_tag_name('area')
# for list in toubu:
#     print(list.text)
















# #选择第一个伤情
driver.switch_to.default_content()
driver.switch_to.frame('rightCmitFrame')
time.sleep(2)
# shangqing2=random.choice(driver.find_elements_by_css_selector('html body div .data-show tbody .tb_tr td input:first-child')).click()
sha=driver.find_element_by_css_selector('html body div .data-show tbody .tb_tr:nth-child(5) td input:first-child')
sha.click()
time.sleep(2)
#点击添加到已选择
tianjia2=driver.find_element_by_css_selector('html body .data .button')
tianjia2.click()
time.sleep(2)
#点击添加到主页面
driver.switch_to.default_content()
driver.switch_to.frame('bottomCmitFrame')
time.sleep(2)
tainjia3=driver.find_element_by_css_selector('html body .data .button')
tainjia3.click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame('mainFrame')
time.sleep(2)
driver.execute_script("window.scrollBy(0,400)", "")
time.sleep(2)

# driver.execute_script(tainjia3)
# # 判断alert弹出框
# result = EC.alert_is_present()(driver)
# if result:
#     result.accept()
# else:
#     driver.quit()



#护理人信息模块儿---------点选亲属
#
# qinshu=driver.find_element_by_css_selector('html body #doLoadFSurvey div:nth-child(20) table #nurseTd table tr td:nth-child(2) option:nth-child(2)').click()
# time.sleep(2)
#
# qsname=driver.find_element_by_css_selector('html body #doLoadFSurvey div:nth-child(20) table #nurseTd table tr td:last-child input')
# qsname.send_keys('亲属姓名')
# time.sleep(2)



#选择任务接收人
jieshou=driver.find_element_by_css_selector('html body #doLoadFSurvey div:nth-child(23) table #rwTd td:last-child .queryUser')
jieshou.click()
time.sleep(2)
driver.switch_to.frame('layui-layer-iframe1')
# driver.switch_to.frame(1)
#定位到李德光，然后双击点选
time.sleep(2)
renren=driver.find_element_by_css_selector('html body .query tbody td:nth-child(4) input')
renren.send_keys('李德光')
time.sleep(2)
cha=driver.find_element_by_css_selector('html body .query tbody td:nth-child(5) input')
cha.click()
time.sleep(2)

shuanji=driver.find_element_by_css_selector('html body .data table tbody tr:nth-child(1) td')
action_chains = ActionChains(driver)
action_chains.double_click(shuanji).perform()
time.sleep(2)
#输入查勘说明
driver.switch_to.default_content()
driver.switch_to.frame('mainFrame')
time.sleep(2)
chakan=driver.find_element_by_css_selector('html body #doLoadFSurvey div:nth-child(23) table tr:last-child td:last-child .textfield')
chakan.send_keys('啊实打实大阿萨德发顺丰十多分1伟大')
time.sleep(3)
#点击提交按钮
tijaio=driver.find_element_by_css_selector('html body #doLoadFSurvey .floatDiv div:last-child input:last-child')
tijaio.click()
time.sleep(3)
#点击确定按钮
queding=driver.find_element_by_css_selector('html body .layui-layer div:last-child .layui-layer-btn0')
queding.click()
time.sleep(5)

content=driver.find_element_by_link_text('百度')




#断言提交结果
# content = driver.find_element_by_css_selector('html body .tab-query tbody tr:first-child td:first-child font')
# a=content.get_attribute('class')
# def a():
#     for link in content:
#         print(link.text)
# message='任务已提交到人伤跟踪平台,当前状态：人伤跟踪待处理，接收人：【演示】北京分部 下的 [演示-北分]查勘岗01'





# if '当前状态' in a:
#     print('成功')
# else:
#     print('失败')











# #选择人伤跟踪--处理任务
# driver.switch_to.window(driver.window_handles[0])
# driver.switch_to.default_content()
# driver.switch_to.frame('leftFrame')
# time.sleep(2)
# gz=driver.find_element_by_css_selector('html body div:nth-child(2) .level1-title')
# gz.click()
# time.sleep(2)
# gs=driver.find_element_by_css_selector('html body div:nth-child(2) .level2-node')
# gs.click()
# time.sleep(2)

#风险信息提醒
# fengxian=driver.find_element_by_css_selector('html body .layui-layer .layui-layer-content div:last-child input')
# fengxian.click()
# time.sleep(2)
# #点击 案件处理 按钮
# driver.switch_to.default_content()
# driver.switch_to.frame('mainFrame')
# chuli=driver.find_element_by_css_selector('html body .info_region td:nth-child(2) input:nth-child(2)')
# chuli.click()
# driver.switch_to.window(driver.window_handles[0])
#
# driver.switch_to.default_content()
# driver.switch_to.frame('mainFrame')
# time.sleep(2)
# # 下一环节：选择跟踪审核
# genzong=driver.find_element_by_css_selector('html body div:nth-child(23) table tr:nth-child(3) td:nth-child(2) option:nth-child(2)')
# genzong.click()
# time.sleep(2)
# #录入跟踪记录
# jilu=driver.find_element_by_css_selector('html body div:nth-child(23) table tr:nth-child(5) .textfield')
# jilu.send_keys("人伤跟踪提交")
# time.sleep(2)
# #跟踪审核提交
# titi=driver.find_element_by_css_selector('html body .floatDiv div:nth-child(2) input:nth-child(2)')
# titi.click()
# time.sleep(2)
# titijiao=driver.find_element_by_css_selector('html body .layui-layer-btn a')
# titijiao.click()
# time.sleep(2)
