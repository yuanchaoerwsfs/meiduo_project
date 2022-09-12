import unittest

from base import BasePage_baidu


class Baidu_Page(BasePage_baidu):
    url = 'https://www.baidu.com'

    def search_open(self):
        self.open(self.url)

    def search_input(self, search_key):
        self.by_id('kw').send_keys(search_key)

    def search_button(self):
        self.by_id('su').click()


if __name__ == '__main__':
    unittest.main()
