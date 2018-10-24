from testsuites.base_testcase import Base_testcase
from pageobjects.luntan_homepage4 import Luntan_homepage4
import  unittest
import time

class LuntanSerach(Base_testcase):
    def test_luntsn_search(self):
        luntan_homepage4 = Luntan_homepage4(self.driver)
        luntan_homepage4.open_url('http://127.0.0.1/upload/forum.php')
        time.sleep(3)
        luntan_homepage4.login('anyong','868686','天气状况','晴天','阴天','雨天')
        time.sleep(3)
if __name__ == '__main__':
    unittest.main()