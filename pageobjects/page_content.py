from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

class PageContent(BasePage):
    # ��λ���+���½�Ԫ��
    page_content_tianjia_input_loc=(By.ID,'com.example.todolist:id/action_new')
    # ��λҪɾ����Ԫ��
    page_content_title_loc=(By.XPATH,'//android.widget.ListView/android.widget.RelativeLayout')
    page_content_longpress_loc = (By.XPATH, '//android.widget.ListView/android.widget.LinearLayout[2]')
    # ��λ���ȷ��Ԫ��
    page_content_check_loc=(By.ID, 'android:id/button1')
    #��λ�˳�Ԫ��
    page_content_quit_input_loc=(By.CLASS_NAME,'android.widget.ImageButton')
    page_content_dianji_input_loc=(By.CLASS_NAME,'android.widget.LinearLayout')
    page_content_queding_input_loc=(By.ID,'android:id/button1')
    #������ + ���½�Ԫ�صķ���
    def add(self):
        self.click(*self.page_content_tianjia_input_loc)
     #���峤��ɾ�����ݵķ���
    def delete(self):
        self.TouchAction(*self.page_content_title_loc)
        self.click(*self.page_content_longpress_loc)
        self.click(*self.page_content_check_loc)
    #�����˳�����
    def quit(self):
        self.click(*self.page_content_quit_input_loc)
        self.click(*self.page_content_dianji_input_loc)
        self.click(*self.page_content_queding_input_loc)

