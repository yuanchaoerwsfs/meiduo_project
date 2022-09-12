from kyb_unittest_Project.common.common_fun import Common
from selenium.webdriver.common.by import By
from kyb_unittest_Project.common.desired_caps import appium_desired
import logging


class LoginView(Common):
    username_type = (By.XPATH, '//*[@class="android.widget.EditText" and @text="请输入用户名"]')
    password_type = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    loginBtn_type = (By.ID, 'com.tal.kaoyan:id/login_login_btn')
    username_clear = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')

    def login_action(self, username, password):
        self.check_updateBtn()
        self.check_skipBtn()
        logging.info("=====================username_clear====================")
        self.driver.find_element(*self.username_clear).clear()

        logging.info("=====================login_username====================")
        logging.info('input username:%s' % username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info("=====================login_password====================")
        logging.info('input password:%s' % password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info("=====================click loginBtn====================")
        self.driver.find_element(*self.loginBtn_type).click()


class RegisterView(Common):
    pass


if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_action('yuanchaoer', 'qq123456')
