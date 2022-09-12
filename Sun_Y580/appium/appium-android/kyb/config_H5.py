from appium import webdriver

desirde_caps = {}

desirde_caps['platformName'] = 'Android'
desirde_caps['deviceName'] = '127.0.0.1:21503'
desirde_caps['platforVersion'] = '5.1.1'

desirde_caps['unicodeKeyboard'] = "True"
desirde_caps['resetKeyboard'] = "True"
desirde_caps['noReset'] = 'True'

# 真机
# desirde_caps['deviceName'] = 'OE106'
# desirde_caps['platforVersion'] = '8.1.0'
# desirde_caps['udid'] = '2b34733d'

desirde_caps['app'] = r'D:\appium_sw\4\H5\dr.fone3.2.0.apk'
desirde_caps['appPackage'] = 'com.wondershare.drfone'
desirde_caps['appActivity'] = 'com.wondershare.drfone.ui.activity.WelcomeActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desirde_caps)
driver.implicitly_wait(3)