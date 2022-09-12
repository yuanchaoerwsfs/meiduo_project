import unittest
import codecs
import csv
from selenium import webdriver
from time import ctime, sleep
from parameterized import parameterized


class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = 'https://www.baidu.com'

    def search_baidu(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        sleep(2)

    @parameterized.expand([('case1', 'selenium'), ('case2', 'unittest'), ('case3', 'parameterized')])
    def test_search_baidu(self, name, search_key):
        print(name)
        self.search_baidu(search_key)
        print(self.driver.title)
        self.assertAlmostEqual(self.driver.title, search_key + '_百度搜索')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
