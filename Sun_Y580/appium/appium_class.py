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

button_list = driver.find_element_by_class_name('android.widget.LinearLayout')
print(len(button_list))

# 打印每个控件的text属性
for button in button_list:
    print(button)

# 操作某一个元素
button_list[8].click()
button_list[16].click()
button_list[2].click()
button_list[11].click()
