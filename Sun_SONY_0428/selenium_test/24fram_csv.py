import csv
from selenium import webdriver
import unittest
from itertools import islice
from time import ctime, sleep
import codecs


class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpclass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = 'https://www.baidu.com'

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        sleep(2)

    def test_search(self):
        with codecs.open('D:/python-test/csv.csv', 'r', 'utf-8') as f:
            data = csv.reader(f)
            for line in islice(data, 1, None):
                search_key = line[1]
                self.baidu_search(search_key)


if __name__ == '__main__':
    unittest.main(verbosity=2)
