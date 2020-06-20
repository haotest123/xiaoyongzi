from selenium.webdriver.common.by import By
from PageObjects.base import BasePage
from framework.logger import Logger
import time

#获取一个loger对象，调用getlog()方法:
logger=Logger(logger="yiban_homepage1").getlog()

#封装了案件详情页面的方法：
class yiban_homepage1(BasePage):

#输入伤者姓名--------------------------------基本信息模块儿
    yiban_homepage1_input_input2_loc=(By.CSS_SELECTOR,'html body #baseInfor table tr:nth-child(6) td:nth-child(2) .textfield')
    #输入联系电话
    yiban_homepage1_input_input3_loc=(By.CSS_SELECTOR,'html body #baseInfor table tr:nth-child(6) td:nth-child(4) .textfield')
    #点选三者类型
    yiban_homepage1_button_button3_loc=(By.CSS_SELECTOR,'html body #baseInfor table tr:nth-child(7) td:nth-child(2) input')
    # #点选人伤归属
    # yiban_homepage1_button_button16_loc=(By.CSS_SELECTOR,'html body #baseInfor table tr:nth-child(7) #injureBelongTd option:last-child')
    #点选责任比例
    yiban_homepage1_button_button10_loc=(By.CSS_SELECTOR,'html body #baseInfor table tr:nth-child(10) td:nth-child(2) .textfield option:nth-child(3)')

#选择户口性质---------------------------参考标准模块儿
    yiban_homepage1_button_select1_loc=(By.CSS_SELECTOR,'html body #referenceStandardDiv table tr td:last-child option:nth-child(2)')

#点击添加诊断----------------------------------诊断信息模块儿
    yiban_homepage1_button_button4_loc=(By.CSS_SELECTOR,'html body #doLoadFSurvey #diagnosisDIV .titleInfo .other .button')

#医院信息--点击增加医院--------------------------医院信息模块儿
    yiban_homepage1_button_button11_loc=(By.CSS_SELECTOR,'html body #doLoadFSurvey #hospitalDIV div .other .button')
    #点击添加就诊医院图标
    yiban_homepage1_button_button12_loc=(By.CSS_SELECTOR,'html body #doLoadFSurvey #hospitalDIV .tab-query tr td:nth-child(2) img')
    #点选就诊医院
    # yiban_homepage1_button_button13_loc=(By.CSS_SELECTOR,'html .body .data-show tr td a')
    #点选门诊/住院日期
    yiban_homepage1_button_button14_loc=(By.CSS_SELECTOR,'html body #doLoadFSurvey #hospitalDIV .tab-query tr td:nth-child(4)')
    #点击今天按钮
    yiban_homepage1_button_button15_loc=(By.CSS_SELECTOR,'html body div #dpControl #dpTodayInput')

#护理信息--点选护理身份：亲属-----------------------护理信息模块儿
    yiban_homepage1_button_button17_loc=(By.CSS_SELECTOR,'html body #doLoadFSurvey div:nth-child(20) table #nurseTd table tr td:nth-child(2) option:nth-child(2)')
    #输入亲属姓名
    yiban_homepage1_input_input4_loc=(By.CSS_SELECTOR,'html body #doLoadFSurvey div:nth-child(20) table #nurseTd table tr td:last-child input')

#死亡信息--点选死亡原因：损伤导致------------------死亡信息模块儿
    yiban_homepage1_button_button18_loc=(By.CSS_SELECTOR,'html body #doLoadFSurvey div:nth-child(16) .tab-query td:nth-child(2) .textfield option:nth-child(2)')
    #点选死亡日期
    yiban_homepage1_button_button19_loc=(By.CSS_SELECTOR,'html body #doLoadFSurvey div:nth-child(16) .tab-query td:last-child .textfield')
    #点击今天按钮
    yiban_homepage1_button_button20_loc=(By.CSS_SELECTOR,'html body div #dpControl #dpTodayInput')

#预估损失明细:后续治疗费
    yiban_homepage1_input_input5_loc=(By.CSS_SELECTOR,'html body #doLoadFSurvey div:nth-child(22) table tbody #feeList04 td:nth-child(4) .textfield')

#点击选择任务接收人图标------------------------查勘记录模块儿
    yiban_homepage1_button_button5_loc=(By.CSS_SELECTOR,'html body #doLoadFSurvey div:nth-child(23) table #rwTd td:last-child .queryUser')
    #输入伤者姓名
    yiban_homepage1_input_input6_loc=(By.CSS_SELECTOR,'html body .query tbody td:nth-child(4) input')
    #点击查询
    yiban_homepage1_button_button21_loc=(By.CSS_SELECTOR,'html body .query tbody td:nth-child(5) input')
    #点选任务接收人
    yiban_homepage1_button_button6_loc=(By.CSS_SELECTOR,'html body .data table tbody tr:nth-child(1) td')
    #输入查勘说明
    yiban_homepage1_button_button7_loc=(By.CSS_SELECTOR,'html body #doLoadFSurvey div:nth-child(23) table tr:last-child td:last-child .textfield')
    #点击提交按钮
    yiban_homepage1_button_button8_loc=(By.CSS_SELECTOR,'html body #doLoadFSurvey .floatDiv div:last-child input:last-child')
    #点击确认按钮
    yiban_homepage1_button_button9_loc=(By.CSS_SELECTOR,'html body .layui-layer div:last-child .layui-layer-btn0')
    #点击风险信息提醒确认按钮
    yiban_homepage1_button_fxtx_loc=(By.CSS_SELECTOR,'html body .layui-layer div:last-child input:first-child')

######################小额人伤#############################
    #预估损失明细：点击添加按钮（小额+无治疗）
    yiban_homepage1_button_buttonYLF_loc=(By.CSS_SELECTOR,'html body #doLoadFSurvey #feeListDIV.titleInfo div:nth-child(2) input')
    #输入查勘说明（小额人伤+无治疗)
    yiban_homepage1_xiaoeshuoming_loc = (By.CSS_SELECTOR, 'html body #doLoadFSurvey div:nth-child(23) table tbody tr:last-child td:last-child .textfield')
    #医疗费信息：估损医疗费（小额+门诊）
    yiban_homepage1_input_ylf_loc=(By.CSS_SELECTOR,'html body #doLoadFSurvey #medicalDiv table tbody tr:first-child td:nth-child(4) input')
    #预估损失明细：误工费（小额+门诊）
    yiban_homepage1_input_wgf_loc=(By.CSS_SELECTOR,'html body #doLoadFSurvey #feeTbody  tr:nth-child(2) td:nth-child(4) input:nth-child(6)')
    #输入查勘说明（小额+门诊)
    yiban_homepage1_textarea_mzshuoming_loc = (By.CSS_SELECTOR, 'html body #doLoadFSurvey div:nth-child(23) table tbody tr:last-child td:last-child .textfield')
    # 输入查勘说明（小额人伤处理页面)
    yiban_homepage1_textarea_xeshuoming_loc = (By.CSS_SELECTOR,'html body div:nth-child(18) table tr:nth-child(3) td:last-child .textfield')
    #点击提交（小额人伤处理页面)
    yiban_homepage1_button_submit_loc = (By.CSS_SELECTOR, 'html body .floatDiv div:last-child input:last-child')
    #确认提交（小额人伤处理页面)
    yiban_homepage1_a_click_loc=(By.CSS_SELECTOR, 'html body .layui-layer-btn0')
    #提交导航提示（小额人伤处理页面）
    yiban_homepage1_font_loc=(By.CSS_SELECTOR,'html body .tab-query tbody tr:first-child td:first-child font')




#封装了基本信息、诊断信息模块儿的方法：
    def xiangqing(self,szname,phone):
        time.sleep(2)
        logger.info('输入伤者姓名')
        self.sendkeys(szname,*self.yiban_homepage1_input_input2_loc)
        time.sleep(2)
        logger.info('输入联系电话')
        self.sendkeys(phone,*self.yiban_homepage1_input_input3_loc)
        time.sleep(2)
        logger.info('点选三者类型')
        self.click(*self.yiban_homepage1_button_button3_loc)
        time.sleep(2)
        # logger.info('点选人伤归属')
        # self.click(*self.yiban_homepage1_button_button16_loc)
        # time.sleep(2)
        logger.info('输入身份证号码')
        self.shenfengzheng()
        time.sleep(2)
        logger.info('点选事故责任')
        self.click(*self.yiban_homepage1_button_button10_loc)
        time.sleep(2)

#封装了参考标准模块儿的方法
    def cankao(self):
        self.click(*self.yiban_homepage1_button_select1_loc)
        time.sleep(2)
        self.alert()
        time.sleep(2)

#封装了添加诊断的方法：
    def zhenduan(self):
        self.driver.execute_script("window.scrollBy(0,200)", "")
        time.sleep(2)
        logger.info('点击添加到诊断')
        self.click(*self.yiban_homepage1_button_button4_loc)
        time.sleep(2)

# 封装了医院信息模块儿的方法：
    def yiyuan(self):
        logger.info('点选增加医院')
        self.driver.execute_script("window.scrollBy(0,400)", "")
        time.sleep(2)
        self.click(*self.yiban_homepage1_button_button11_loc)
        time.sleep(2)
        logger.info('点击添加就诊医院图标')
        self.click(*self.yiban_homepage1_button_button12_loc)
        time.sleep(2)
        self.driver.switch_to.frame('layui-layer-iframe1')
        time.sleep(2)
        logger.info('单击击就诊医院')
        self.click1()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        logger.info('点选门诊/住院日期')
        self.click(*self.yiban_homepage1_button_button14_loc)
        logger.info('点选日期')
        time.sleep(2)
        self.driver.switch_to.frame(1)
        time.sleep(2)
        logger.info('点选日期为当天的日期')
        self.click(*self.yiban_homepage1_button_button15_loc)
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        time.sleep(2)

#封装了护理信息模块儿的方法：
    def huli(self,qsname):
        self.actity3_window()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        time.sleep(2)
        logger.info('点选护理人身份--亲属')
        self.click(*self.yiban_homepage1_button_button17_loc)
        time.sleep(2)
        logger.info('输入护理人姓名')
        self.sendkeys(qsname,*self.yiban_homepage1_input_input4_loc)
        time.sleep(2)
#封装了死亡信息模块儿的方法：
    def siwang(self):
        self.actity3_window()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        time.sleep(2)
        logger.info('点选死亡原因--损伤导致')
        self.click(*self.yiban_homepage1_button_button18_loc)
        time.sleep(2)
        logger.info('点选死亡日期')
        self.click(*self.yiban_homepage1_button_button19_loc)
        time.sleep(2)
        self.driver.switch_to.frame(1)
        time.sleep(2)
        logger.info('点选死亡日期---今天')
        self.click(*self.yiban_homepage1_button_button20_loc)
        time.sleep(2)

#封装了预估损失明细:后续治疗费 的方法：
    def yugu(self,zhuyuan):
        self.driver.execute_script("window.scrollBy(0,600)", "")
        time.sleep(2)
        logger.info('输入后续治疗费')
        self.sendkeys(zhuyuan,*self.yiban_homepage1_input_input5_loc)
        time.sleep(2)

# 封装了查勘记录模块儿方法（门诊治疗/住院治疗）：
    def chakan(self,yhname):
        self.actity3_window()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,400)", "")
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        time.sleep(2)
        logger.info('点选任务接收人图标')
        time.sleep(2)
        self.click(*self.yiban_homepage1_button_button5_loc)
        time.sleep(2)
        self.driver.switch_to.frame('layui-layer-iframe2')
        time.sleep(2)
        logger.info('输入用户姓名')
        self.sendkeys(yhname, *self.yiban_homepage1_input_input6_loc)
        time.sleep(2)
        logger.info('点击查询按钮')
        self.click(*self.yiban_homepage1_button_button21_loc)
        time.sleep(2)
        logger.info('双击任务接收人')
        self.doubleclick(*self.yiban_homepage1_button_button6_loc)
        time.sleep(2)

# 封装了查勘记录模块儿的方法（无治疗）：
    def chakan1(self,yhname1):
        self.actity3_window()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,600)", "")
        logger.info('点选任务接收人图标')
        time.sleep(2)
        self.click(*self.yiban_homepage1_button_button5_loc)
        time.sleep(2)
        self.driver.switch_to.frame('layui-layer-iframe1')
        time.sleep(2)
        logger.info('输入用户姓名')
        self.sendkeys(yhname1, *self.yiban_homepage1_input_input6_loc)
        time.sleep(2)
        logger.info('点击查询按钮')
        self.click(*self.yiban_homepage1_button_button21_loc)
        time.sleep(2)
        logger.info('双击任务接收人')
        self.doubleclick(*self.yiban_homepage1_button_button6_loc)
        time.sleep(2)


#封装了查勘记录模块儿明以及案件进行提交的方法
    def tijiao(self,shuoming):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        logger.info('输入查勘说明')
        self.sendkeys(shuoming, *self.yiban_homepage1_button_button7_loc)
        time.sleep(2)
        logger.info('点击提交按钮')
        self.click(*self.yiban_homepage1_button_button8_loc)
        time.sleep(2)
        logger.info('点击确认按钮')
        self.click(*self.yiban_homepage1_button_button9_loc)
        time.sleep(3)
        self.runfengxian()
        time.sleep(2)
        self.Submit()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        time.sleep(2)



#######################小额人伤相关方法#################################

#封装了预估损失明细（小额人伤+无治疗）：
    def yuguXiaoe(self):
        self.actity3_window()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,600)", "")
        time.sleep(2)

#封装了查勘记录以及案件提交方法（小额人伤+无治疗）
    def JiluAndSubmitW(self,shuoming):
        logger.info('输入查勘说明')
        self.sendkeys(shuoming, *self.yiban_homepage1_xiaoeshuoming_loc)
        time.sleep(2)
        logger.info('点击提交按钮')
        self.click(*self.yiban_homepage1_button_button8_loc)
        time.sleep(2)
        logger.info('点击确认按钮')
        self.click(*self.yiban_homepage1_button_button9_loc)
        time.sleep(3)

        self.runfengxian()
        logger.info('执行小额无治疗案件提交')
        self.Submit()
        time.sleep(2)

#封装了查勘记录以及案件提交方法（小额人伤+门诊）

    def JiluAndSubmitM(self,shuoming):
        logger.info('输入查勘说明')
        self.sendkeys(shuoming, *self.yiban_homepage1_textarea_mzshuoming_loc)
        time.sleep(2)
        logger.info('点击提交按钮')
        self.click(*self.yiban_homepage1_button_button8_loc)
        time.sleep(2)
        logger.info('点击确认按钮')
        self.click(*self.yiban_homepage1_button_button9_loc)
        time.sleep(3)
        self.runfengxian()
        logger.info('执行小额门诊/住院案件提交')
        self.Submit()
        time.sleep(2)

#封装医疗费+误工费（小额人伤）
    def xiaoeSubmit(self,ylf,wgf):
        self.actity3_window()
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame('mainFrame')
        time.sleep(2)
        logger.info('编辑估损医疗费')
        self.sendkeys(ylf, *self.yiban_homepage1_input_ylf_loc)
        time.sleep(2)
        logger.info('编辑误工费')
        self.sendkeys(wgf, *self.yiban_homepage1_input_wgf_loc)
        time.sleep(2)
#封装了小额备注以及案件提交方法（小额人伤处理页面）
    def beizhuAndSubmit(self,shuoming):
        logger.info('输入小额人伤备注')
        self.sendkeys(shuoming, *self.yiban_homepage1_textarea_xeshuoming_loc)
        time.sleep(2)
        logger.info('点击提交按钮')
        self.click(*self.yiban_homepage1_button_submit_loc)
        time.sleep(2)
        logger.info('点击确定按钮')
        self.click(*self.yiban_homepage1_a_click_loc)
        time.sleep(2)
        #self.runfengxian()
        logger.info('执行小额人伤提交')
        self.Submit()
        time.sleep(2)










































