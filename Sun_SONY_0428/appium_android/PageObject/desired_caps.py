import logging.config
import yaml
from appium import webdriver

CON_LOG = './config_log'  # config_log.yaml 路径
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


def appium_desired():
    file = open('./config_yaml', 'r')
    data = yaml.safe_load(file)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']

    desired_caps['platformVersion'] = data['platforVersion']
    desired_caps['deviceName'] = data['deviceName']

    desired_caps['app'] = data['app']
    desired_caps['noReset'] = data['noReset']

    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    logging.info('start APP .....')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    return driver


if __name__ == '__main__':
    appium_desired()
