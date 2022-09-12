from poium_Baidu_page import poium_BaiduPage
import unittest
from selenium import webdriver
from time import sleep


class TestBaidu_poium(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.base_url = 'http://www.baidu.com'

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_baidu_search_case1(self):
        page = poium_BaiduPage(self.driver)
        page.get('http://www.baidu.com')
        page.search_input = 'selenium'
        page.search_button.click()
        sleep(2)
        self.assertEqual(page.get_title(), 'selenium_百度搜索')


if __name__ == '__main__':
    unittest.main(verbosity=2)
