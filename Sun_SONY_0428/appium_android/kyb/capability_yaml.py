import logging
import logging.config
import yaml
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

file = open('config_yaml', 'r')
data = yaml.safe_load(file)

CON_LOG = 'config_log'   #config_log.yaml 路径
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

desired_caps = {}
desired_caps['platformName'] = data['platformName']

desired_caps['platformVersion'] = data['platforVersion']
desired_caps['deviceName'] = data['deviceName']

desired_caps['app'] = data['app']
desired_caps['noReset'] = data['noReset']

desired_caps['appPackage'] = data['appPackage']
desired_caps['appActivity'] = data['appActivity']
logging.info('start APP .....')
driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)


def check_cancelBtn():
    logging.info("check_cancelBtn")
    try:
        cancleBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        logging.info("No cancelBtn")
    else:
        cancleBtn.click()
        driver.implicitly_wait(3)


def check_skipBtn():
    logging.info("check_skinBtn")
    try:
        SkinBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        logging.info('No SkinBtn')
    else:
        SkinBtn.click()
        driver.implicitly_wait(3)


check_cancelBtn()
check_skipBtn()
