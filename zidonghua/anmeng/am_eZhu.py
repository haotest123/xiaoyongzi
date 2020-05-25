from zidonghua.base_testcase import base_testcase
from PageObjects.caidan_shouciHomepage1 import shouci_homepage1
from PageObjects.yiban_Homepage1 import yiban_homepage1
from PageObjects.zhenduan_homepage import zhenduan_homepage
from PageObjects.jiuzhen_type import jiuzhen
from framework.logger import Logger

# from zidonghua.Log_SendMail import SendEmail
# import warnings



#获取一个loger对象，调用getlog()方法:
logger=Logger(logger="xiaoeZhu").getlog()

class xiaoeMen(base_testcase):

    def test_xiaoeMen(self):
        logger.info('--------------------------小额人伤+住院治疗场景开始执行-----------------------')
        # 点击首次查勘---处理任务，选择处理中后点击查询按钮后，点击第一个案件---报案号，进入案件详情页：
        xiaoeMen=shouci_homepage1(self.driver)
        xiaoeMen.shouci()

        # 进入案件详情页的操作--------点选事故类型,点选损失类型为：小额人伤，点选就诊类型为：门诊治疗
        xiaoeMen = jiuzhen(self.driver)
        xiaoeMen.xiaoeZhu()


        #输入伤者姓名、联系电话，点选三者类型，
        #点击添加诊断按钮，进入诊断伤情页面 ：
        xiaoeMen=yiban_homepage1(self.driver)
        xiaoeMen.xiangqing('小额住院自动化','13681288321')
        xiaoeMen.yiyuan()
        xiaoeMen.zhenduan()

        #进入诊断详情页面的操作------输入某一伤情名称，点击查询按钮，选择一诊断伤情点击添加到已选择，随后点击添加到主页面：
        xiaoeMen=zhenduan_homepage(self.driver)
        xiaoeMen.shangqing('擦伤')

        #输入医疗费和误工费
        xiaoeMen = yiban_homepage1(self.driver)
        xiaoeMen.xiaoeSubmit(100,1)

        #输入查勘记录并提交
        xiaoeMen = yiban_homepage1(self.driver)
        xiaoeMen.JiluAndSubmitM('小额人伤住院治疗查勘记录')

        logger.info('--------------------------小额人伤+住院治疗场景执行完毕-----------------------')







