from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:21503'
desired_caps['platforVersion'] = '5.1.1'

desired_caps['unicodeKeyboard'] = "True"
desired_caps['resetKeyboard'] = "True"
desired_caps['noReset'] = 'True'

# 真机
# desired_caps['deviceName'] = 'OE106'
# desired_caps['platforVersion'] = '8.1.0'
# desired_caps['udid'] = '2b34733d'

desired_caps['app'] = r'D:\appium_software\4\H5\dr_fone3.2.0.apk'
desired_caps['appPackage'] = 'com.wondershare.drfone'
desired_caps['appActivity'] = 'com.wondershare.drfone.ui.activity.WelcomeActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(3)

print('click BackupBtn')
driver.find_element_by_id('com.wondershare.drfone:id/btnBackup').click()

WebDriverWait(driver, 8).until(lambda x: x.find_element_by_id('com.wondershare.drfone:id/btnRecoverData'))
print('click NextBtn')
driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()

WebDriverWait(driver, 8).until(lambda x: x.find_element_by_class_name('android.webkit.WebView'))
contexts = driver.contexts
print(contexts)
