from appium_android_SONY.PageObject.baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
from appium_android_SONY.PageObject.desired_caps import appium_desired
from appium import webdriver


class Common(BaseView):
    cancelBtn = (By.ID, 'android:id/button2')
    skipBtn = (By.ID, 'com.tal.kaoyan:id/tv_skip')

    def check_cancelBtn(self):
        logging.info("======================check_cancelBtn=========================")
        try:
            element = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info("=========No cancelBtn========")
        else:
            logging.info('----click_cancelBtn----')
            element.click()

    def check_skipBtn(self):
        logging.info("======================check_skinBtn======================")
        try:
            element = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('=========No SkinBtn========')
        else:
            logging.info('----click_skipBtn----')
            element.click()


if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    com.check_cancelBtn()
    com.check_skipBtn()
