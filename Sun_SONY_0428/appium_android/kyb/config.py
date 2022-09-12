from appium import webdriver

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62025'
desired_caps['platforVersion'] = '5.1.1'
desired_caps['automationName']='uiautomator2'   #Toast  支持

desired_caps['unicodeKeyboard'] = "True"
desired_caps['resetKeyboard'] = "True"
desired_caps['noReset'] = 'True'

# 真机
# desired_caps['deviceName'] = 'OE106'
# desired_caps['platforVersion'] = '8.1.0'
# desired_caps['udid'] = '2b34733d'

desired_caps['app'] = r'D:\appium_software\4\App\kaoyan3.1.0.apk'
desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(3)