from zidonghua.base_testcase import base_testcase
from PageObjects.caidan_shouciHomepage1 import shouci_homepage1
from PageObjects.yiban_Homepage1 import yiban_homepage1
from PageObjects.zhenduan_homepage import zhenduan_homepage
from PageObjects.jiuzhen_type import jiuzhen
from framework.logger import Logger

# from zidonghua.Log_SendMail import SendEmail
# import warnings



#获取一个loger对象，调用getlog()方法:
logger=Logger(logger="xiaoeWu").getlog()

class xiaoeWu(base_testcase):

    def test_yibanWu(self):
        logger.info('--------------------------小额人伤+无治疗场景开始执行-----------------------')
        # 点击首次查勘---处理任务，选择处理中后点击查询按钮后，点击第一个案件---报案号，进入案件详情页：
        xiaoeWu=shouci_homepage1(self.driver)
        xiaoeWu.shouci()

        # 进入案件详情页的操作--------点选事故类型,点选损失类型为：小额人伤，点选就诊类型为：无治疗
        xiaoeWu = jiuzhen(self.driver)
        xiaoeWu.xiaoeWu()


        #输入伤者姓名、联系电话，点选三者类型，
        #点击添加诊断按钮，进入诊断伤情页面 ：
        xiaoeWu=yiban_homepage1(self.driver)
        xiaoeWu.xiangqing('小额无治疗自动化','13681288321')
        xiaoeWu.zhenduan()

        #进入诊断详情页面的操作------输入某一伤情名称，点击查询按钮，选择一诊断伤情点击添加到已选择，随后点击添加到主页面：
        xiaoeWu=zhenduan_homepage(self.driver)
        #xiaoeWu.shangqing1()
        xiaoeWu.shangqing('擦伤')

        #添加医疗费，点击提交按钮，弹出的页面点击确认按钮
        xiaoeWu = yiban_homepage1(self.driver)
        xiaoeWu.yuguXiaoe()
        xiaoeWu.JiluAndSubmitW('小额人伤无治疗场景相关查勘说明')
        logger.info('--------------------------小额人伤+无治疗场景执行完毕-----------------------')







