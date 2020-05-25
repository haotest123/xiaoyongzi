from zidonghua.base_testcase import base_testcase
from PageObjects.caidan_shouciHomepage1 import shouci_homepage1
from PageObjects.yiban_Homepage1 import yiban_homepage1
from PageObjects.zhenduan_homepage import zhenduan_homepage
from PageObjects.jiuzhen_type import jiuzhen
from framework.logger import Logger



#获取一个loger对象，调用getlog()方法:
logger=Logger(logger="yibanMen").getlog()

class yibanMen(base_testcase):
    def test_yibanMen(self):
        logger.info('--------------------------一般损伤+门诊治疗场景开始执行-----------------------')
        # 点击首次查勘---处理任务，选择处理中后点击查询按钮后，点击第一个案件---报案号，进入案件详情页：
        yibanMen_homepage1=shouci_homepage1(self.driver)
        yibanMen_homepage1.shouci()

        # 进入案件详情页的操作--------点选事故类型,点选损失类型为：一般损伤，点选就诊类型为：门诊治疗
        yibanMen_homepage1 = jiuzhen(self.driver)
        yibanMen_homepage1.yibanMen()
        #输入伤者姓名、联系电话，点选三者类型，
        #点击添加诊断按钮，进入诊断伤情页面 ：
        yibanMen_homepage1=yiban_homepage1(self.driver)
        yibanMen_homepage1.xiangqing('一般门诊自动化','88888888')
        yibanMen_homepage1.yiyuan()
        yibanMen_homepage1.zhenduan()


        #进入诊断详情页面的操作------输入某一伤情名称，点击查询按钮，选择一诊断伤情点击添加到已选择，随后点击添加到主页面：
        yibanMen_homepage1=zhenduan_homepage(self.driver)
        yibanMen_homepage1.shangqing1()

        #点选任务接收人，点击提交按钮，弹出的页面点击确认按钮
        yibanMen_homepage1 = yiban_homepage1(self.driver)
        yibanMen_homepage1.chakan('李德光')
        yibanMen_homepage1.tijiao('一般损伤+门诊治疗 场景提交')
        logger.info('--------------------------一般损伤+门诊治疗场景执行完毕-----------------------')



