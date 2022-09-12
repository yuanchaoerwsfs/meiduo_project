import unittest
from time import ctime, sleep
from selenium import webdriver


class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = 'https://www.baidu.com/'

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        sleep(1)
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        sleep(2)

    def test_selenium(self):
        search_key = 'selenium'
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索')

    def test_unittest(self, ):
        unittest_key = 'unittest'
        self.baidu_search(unittest_key)
        self.assertEqual(self.driver.title, unittest_key + '_百度搜索')

    @classmethod
    def tearDownClass(cls) -> object:
        cls.driver.quit()


if __name__ == '__main__'"":
    unittest.main()
