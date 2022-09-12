import sys
from time import sleep
from selenium import webdriver
from os.path import dirname,abspath
from page.baidu_page import BaiduPage

class TeatSearch():
    """百度搜索"""
    def test_baidu_search_case(self,browser,base_url):
        """百度搜索：pytest"""
        page=BaiduPage(browser)
        page.get(base.url)
        page.search_input('pytest')
        page.search_button.click()
        sleep(2)
        assert browser.title=='pytest_百度搜索'

