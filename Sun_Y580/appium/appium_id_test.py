from appium import webdriver

# 定义运行环境
desired_caps = {
    'deviceName': 'Android Emulator',
    'automationName': 'appium',
    'platformName': 'Android',
    'platformVersion': '7.0',
    'appPackage': 'com.android.calculator2',
    'appActivity': '.Calculator',
    'noReset': 'false'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.install_app('E:\weixin_1560.apk')

driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
driver.find_element_by_id('com.android.calculator2:id/op_add').click()
driver.find_element_by_id('com.android.calculator2:id/digit_2').click()
driver.find_element_by_id('com.android.calculator2:id/eq').click()

driver.quit()
