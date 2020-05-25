from zidonghua.base_testcase import base_testcase
from PageObjects.caidan_shouciHomepage1 import shouci_homepage1
from PageObjects.yiban_Homepage1 import yiban_homepage1
from PageObjects.zhenduan_homepage import zhenduan_homepage
from PageObjects.jiuzhen_type import jiuzhen
from framework.logger import Logger

# from zidonghua.Log_SendMail import SendEmail
# import warnings



#获取一个loger对象，调用getlog()方法:
logger=Logger(logger="xiaoerenshang").getlog()

class xiaoerenshang(base_testcase):
    def test_xiaoeMen(self):
        logger.info('--------------------------小额人伤处理场景开始执行-----------------------')

        # 点击小额人伤---处理任务，选择处理后点击查询按钮后，点击第一个案件---报案号，进入案件详情页：
        xiaoers=shouci_homepage1(self.driver)
        #xiaoers.close()
        xiaoers.xiaoe('小额住院自动化')

        #输入小额人伤备注并提交
        xiaoers=yiban_homepage1(self.driver)
        xiaoers.beizhuAndSubmit('小额人伤处理备注')

        logger.info('--------------------------小额人伤处理场景执行完毕-----------------------')







