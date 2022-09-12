from time import ctime, sleep
import unittest
from selenium import webdriver
from itertools import islice
import codecs
import csv


class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = 'https://www.baidu.com'
        cls.test_data = []
        with codecs.open('csv.csv', 'r', 'utf-8')as f:
            data = csv.reader(f)
            for line in islice(data, 1, None):
                cls.test_data.append(line)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        sleep(2)

    def test_search_selenium(self):
        self.baidu_search(self.test_data[0][1])

    def test_search_unittest(self):
        self.baidu_search(self.test_data[1][1])

    def test_search_parameterized(self):
        self.baidu_search(self.test_data[2][1])


if __name__ == '__main__':
    unittest.main(verbosity=2)
