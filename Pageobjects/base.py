from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from framework.logger import Logger
import os.path
import time


import re
import random
from datetime import timedelta, date
id_code_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
check_code_list = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
class IDcard(object):
    def is_id_card(id_number):
        if len(id_number) != 18:
            return False, "Length error"
        if not re.match(r"^\d{17}(\d|X|x)$", id_number):
            return False, "Format error"
        try:
            date(int(id_number[6:10]), int(id_number[10:12]), int(id_number[12:14]))
        except ValueError as ve:
            return False, "Datetime error: {0}".format(ve)
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


#获取一个loger对象，调用getlog()方法:
logger=Logger(logger="BasePage").getlog()

class BasePage(object):
    # login_url='http://127.0.0.1/upload/forum.php'
    #初始化页面
    def __init__(self,driver):
        self.driver=driver

     # 浏览器打开一个页面
    def open_url(self,url):
        self.driver.get(url)
        #浏览器关闭并推出
    # def quit_browser(self):
    #     self.driver.quit()
    def close(self):
        try:
            self.driver.close()
            logger.info('关闭并退出浏览器')
        except Exception as e:
            logger.error('退出浏览器发生错误%s',e)
     #一个*是元组，两个*是字典
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info('执行成功',loc)
        except:
            logger.error('执行失败%s',(self,loc))

    #保存图片
    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath('.'))+ '/screenshots/'
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        # 全路径
        screen_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info('截得的图片保存在文件夹')
        except Exception as e:
            self.get_windows_img()
            logger.error('截图发生了错误%s',e)
    #进行输入内容
    def sendkeys(self,text,*loc):
        element=self.find_element(*loc)
        element.clear()
        try:
            element.send_keys(text)
            logger.info('执行成功')
            #logger.info('执行成功%s',element.text)
            #logger.info('开始进行输入%s',element.text)
        except:
            logger.error('执行失败%s',(self,loc))

    def doubleclick(self,*loc):
        element=self.find_element(*loc)
        try:
            action_chains = ActionChains(self.driver)
            action_chains.double_click(element).perform()
            logger.info('双击正确')
        except:
            logger.error('双击失败')


    #清除文本框:
    def clear(self,*loc):
        element=self.find_element(*loc)
        element.clear()
        try:
            element.clear()
        except:
            logger.erron('清除元素未找到%s', (self, loc))

    # 点击元素
    def click(self, *loc):
        element = self.find_element(*loc)
        try:
            logger.info('执行成功')
            element.click()
        except  Exception as e:
            logger.error('执行失败', e)

    # 点击随机元素（多种元素随机点击一个-------医院）
    def click1(self):
        element=random.choice(self.driver.find_elements_by_css_selector('html .body .data-show tr td a'))
        try:
            logger.info('执行成功')
            element.click()
        except  Exception as e:
            logger.error('执行失败', e)

#窗口切换
    def actity_window(self):
        try:
            self.driver.switch_to.window(self.driver.current_window_handle)
            logger.info('激活当前窗口')
        except:
            logger.error('激活窗口失败')
    def actity1_window(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            logger.info('激活当前窗口')
        except:
            logger.error('激活窗口失败')
    def actity2_window(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[2])
            logger.info('激活当前窗口')
        except:
            logger.error('激活窗口失败')
#激活主窗口页面方法
    def actity3_window(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[0])
            logger.info('激活当前窗口')
        except:
            logger.error('激活窗口失败')
#iframe嵌套
    def in_moudle(self,content):
        try:
            self.driver.switch_to.frame(content)
            logger.info('进入iframe模块正确')
        except:
            logger.error('进入iframe模块错误')
    def quit_moudle(self):
        try:
            self.driver.switch_to.default_content()
            logger.info('跳出iframe模块正确')
        except:
            logger.error('跳出iframe模块错误')

    #断言标题是否存在
    def element_in_title(self,content,*loc):
        self.content = self.find_element(*loc)
        try:
            assert content in self.driver.title
            logger.info('标题正确')
        except:
            logger.error('标题错误')


   # 断言提交是否成功
    def Submit(self):
        content=self.driver.find_element_by_css_selector('html body .tab-query tbody tr:first-child td:first-child font').text
        try:
            assert u'当前状态' in content
        except AssertionError:
            logger.error('提交结果失败')
        else:
            logger.info('提交结果成功')

# 投票选取方法
    def element_output_title(self,*loc):
        element= self.find_element(*loc)
        try:
            logger.info('The element %s was print' %element.text)
        except:
            logger.error('元素没有选取成功')
#浏览器alert弹框的方法：
    def alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()
###################查询列表，手机小图标处理########################################
    # 有手机图标的方法
    def icon(self):
        self.iconNo()
        alert = self.driver.switch_to.alert()
        time.sleep(2)
        alert.accept()
        time.sleep(2)
        self.iconNo()
    # 无手机图标的方法
    def iconNo(self):
        baoan2 = self.driver.find_element_by_css_selector('html body .data .data-show tbody tr td a')
        time.sleep(2)
        baoan2.click()
        time.sleep(2)
    # 调用有无手机图标的方法
    def phone_icon(self):
        try:
            firstImg = self.driver.find_element_by_css_selector('html body .data .data-show tbody tr td:nth-child(7) img')
        except NoSuchElementException :
            logger.info('无手机图标')
            self.iconNo()
        else:
            logger.info('有手机图标')
            self.icon()

###############################案件提交时，风险规则提示处理##################################################
    def runnotfx(self):
        logger.info('无风险提醒')
        time.sleep(2)

    def runfx(self):
        fxBtn1_loc = self.driver.find_element_by_css_selector('html body .layui-layer div:last-child input:first-child')
        logger.info('点击风险提醒-确定按钮')
        fxBtn1_loc.click()
        time.sleep(2)

    def runfengxian(self):
        try:
            fxBtn =self.driver.find_element_by_css_selector('html body .layui-layer div:last-child input:first-child')
        except NoSuchElementException:
            logger.info('无风险提示弹框')
            self.runnotfx()
        else:
            logger.info('有风险提示弹框')
            self.runfx()

########################输入任意随机有效的身份证号#####################：
    def shenfengzheng(self):
        ID=self.driver.find_element_by_css_selector('html body #doLoadFSurvey .info_region table tr:nth-child(8) td:nth-child(4) input')
        ID.clear()
        area_code = random.choice(["420102", "420103", "420104", "420105", "420106", "420107"])
        IDc = IDcard.gen_id_card(area_code, 22, 1)
        ID.send_keys(IDc)
        time.sleep(2)

























