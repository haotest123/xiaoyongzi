from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

class  PageNewConstruction(BasePage):
    # ��λ�½����ݿ�Ԫ��
    page_newconstruction_input_loc=(By.ID,'com.example.todolist:id/toDoItemDetailET')
    # ��λ����Ԫ��
    page_newconstruction_save_loc=(By.CLASS_NAME,'android.widget.Button')

    # �����½��������񷽷�
    def newConstruction(self,content):
        self.sendkeys(content,*self.page_newconstruction_input_loc)
        self.click(*self.page_newconstruction_save_loc)
