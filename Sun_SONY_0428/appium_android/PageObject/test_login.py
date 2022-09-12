from appium_android.PageObject.myunit import StartEnd
from appium_android.PageObject.loginView import LoginView
import unittest
import logging


class TestLogin(StartEnd):

    def test_login_yuanchaoer(self):
        logging.info('==========test_login_yuanchaoer==========')
        l = LoginView(self.driver)
        l.login_action('yuanchaoer', 'qq123456')

    def test_login_zxw2018(self):
        logging.info('==========test_login_zxw2018==========')
        l = LoginView(self.driver)
        l.login_action('自学网2018', 'zxw2018')

    def test_login_error(self):
        logging.info('==========test_login_error==========')
        l = LoginView(self.driver)
        l.login_action('666666', '222222')


if __name__ == '__main__':
    unittest.main()
