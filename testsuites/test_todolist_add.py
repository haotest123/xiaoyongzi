from testsuites.base_testcase import Base_testcase
from pageobjects.page_login import PageLogin
from pageobjects.page_new_construction import PageNewConstruction
from pageobjects.page_content import PageContent
import unittest

class TodolistLogin(Base_testcase):
    def test_todolist_login(self):
        page_login=PageLogin(self.driver)
        #输入用户名和密码开始登录
        page_login.login('1','1')
        #点击+号开始新建
        page_content=PageContent(self.driver)
        page_content.add()
        #新建待办事务
        page_new_construction=PageNewConstruction(self.driver)
        page_new_construction.newConstruction('aaaaaa')
        #退出
        page_content.quit()
if __name__=='__main__':
    unittest.main()



























