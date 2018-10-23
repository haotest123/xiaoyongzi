from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

class PageContent(BasePage):
    # 定位点击+号新建元素
    page_content_tianjia_input_loc=(By.ID,'com.example.todolist:id/action_new')
    # 定位要删除的元素
    page_content_title_loc=(By.XPATH,'//android.widget.ListView/android.widget.RelativeLayout')
    page_content_longpress_loc = (By.XPATH, '//android.widget.ListView/android.widget.LinearLayout[2]')
    # 定位点击确定元素
    page_content_check_loc=(By.ID, 'android:id/button1')
    #定位退出元素
    page_content_quit_input_loc=(By.CLASS_NAME,'android.widget.ImageButton')
    page_content_dianji_input_loc=(By.CLASS_NAME,'android.widget.LinearLayout')
    page_content_queding_input_loc=(By.ID,'android:id/button1')
    #定义点击 + 号新建元素的方法
    def add(self):
        self.click(*self.page_content_tianjia_input_loc)
     #定义长按删除内容的方法
    def delete(self):
        self.TouchAction(*self.page_content_title_loc)
        self.click(*self.page_content_longpress_loc)
        self.click(*self.page_content_check_loc)
    #定义退出方法
    def quit(self):
        self.click(*self.page_content_quit_input_loc)
        self.click(*self.page_content_dianji_input_loc)
        self.click(*self.page_content_queding_input_loc)

