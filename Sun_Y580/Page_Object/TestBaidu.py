import unittest
from time import sleep
from selenium import webdriver
from baidu_Page import Baidu_Page


class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.base_url = 'http://www.baidu.com'

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_baidu_search_case(self):
        page = Baidu_Page(self.driver)
        page.search_open()
        page.search_input('selenium')
        page.search_button()
        sleep(2)
        self.assertEqual(page.get_title(), 'selenium_百度搜索')


if __name__ == '__main__':
    unittest.main(verbosity=2)
