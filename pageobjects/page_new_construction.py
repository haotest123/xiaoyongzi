from pageobjects.base import BasePage
from selenium.webdriver.common.by import By

class  PageNewConstruction(BasePage):
    # 定位新建内容框元素
    page_newconstruction_input_loc=(By.ID,'com.example.todolist:id/toDoItemDetailET')
    # 定位保存元素
    page_newconstruction_save_loc=(By.CLASS_NAME,'android.widget.Button')

    # 定义新建待办事务方法
    def newConstruction(self,content):
        self.sendkeys(content,*self.page_newconstruction_input_loc)
        self.click(*self.page_newconstruction_save_loc)
