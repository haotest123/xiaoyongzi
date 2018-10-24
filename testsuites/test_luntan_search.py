from testsuites.base_testcase import Base_testcase
from pageobjects.luntan_homepage3 import Luntan_homepage3
import unittest
import time


class LuntanSerach(Base_testcase):
    def test_luntsn_search(self):
        luntan_homepage3 = Luntan_homepage3(self.driver)
        luntan_homepage3.open_url('http://127.0.0.1/upload/forum.php')
        time.sleep(3)
        luntan_homepage3.login('anyong','868686','haotest','haotest')
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
