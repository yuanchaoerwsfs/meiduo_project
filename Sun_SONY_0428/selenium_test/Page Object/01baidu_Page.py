from base_01 import BasePage_baidu

class BaiduPage(BasePage):
    url = 'https://www.baidu.com'

    def search_input(self, search_key):
        self.by_id('kw').send_key(search_key)

    def search_button(self):
        self.by_id('su').click()
