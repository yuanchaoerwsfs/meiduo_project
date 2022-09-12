import unittest
from model import function, myunit
from page_object.LoginPage import *
from time import sleep


class LoginTest(myunit.StartEnd):
    # @unittest.skip('skip this case')
    def test_login1_normal(self):
        '''username and passwd is normal'''
        print("test_login1_normal is start test...")
        po = LoginPage(self.driver)
        po.Login_action('51zxw', 123456)
        sleep(2)

        self.assertEqual(po.type_loginPass_hint(), '我的空间')
        function.insert_img(self.driver, "51zxw_login1_normal.jpg")
        print("test_login1_normal test end!")

    # @unittest.skip('skip this case')
    def test_login2_PasswdError(self):
        '''username is ok,passwd is error'''
        print("test_login2_passwdError is start test...")
        po = LoginPage(self.driver)
        po.Login_action('51zxw', 3333)
        sleep(2)

        self.assertEqual(po.type_loginFail_hint(), '')
        function.insert_img(self.driver, "test_login2_PasswdError.jpg")

    def test_login3_empty(self):
        '''username and passwd is empty'''
        print("test_login3_empty is start test...")
        po = LoginPage(self.driver)
        po.Login_action('', '')
        sleep(2)

        self.assertEqual(po.type_loginFail_hint(), '')
        function.insert_img(self.driver, 'test_login3_empty.jpg')
        print("test_login3_empty test end")


if __name__ == '__main__':
    unittest.main()
