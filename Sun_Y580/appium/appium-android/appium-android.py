from appium import webdriver
from time import sleep

# 定义运行环境
desired_caps = {
    'deviceName': 'Pixel',
    'automationName': 'appium',
    'platformName': 'Android',
    'platformVersion': '7.0',
    'appPackage': 'com.android.calculator2',
    'appActivity': '.Calculator',
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

driver.find_element_by_id('com.android.calculator2:id/digit_5').click()
driver.find_element_by_id('com.android.calculator2:id/op_mul').click()
driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
driver.find_element_by_id('com.android.calculator2:id/eq').click()

sleep(10)
driver.quit()
