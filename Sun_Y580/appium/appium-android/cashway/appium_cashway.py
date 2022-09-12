from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desirde_caps = {}

desirde_caps['platformName'] = 'Android'
desirde_caps['deviceName'] = '127.0.0.1:62001'
desirde_caps['platforVersion'] = '5.1.1'

desirde_caps['noReset'] = 'True'

# 真机
# desirde_caps['deviceName'] = 'OE106'
# desirde_caps['platforVersion'] = '8.1.0'
# desirde_caps['udid'] = '2b34733d'

desirde_caps['app'] = r'D:\appium_software\Cashway Android TJ Bank Advertising Machine Agent APP V1.8.2.2[20200311].apk'
desirde_caps['appPackage'] = 'com.cashway.show'
desirde_caps['appActivity'] = 'com.cashway.show.HomeDexActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desirde_caps)
driver.implicitly_wait(5)

root_element = driver.find_element_by_id('com.cashway.show:id/custom')
root_element.find_element_by_class_name('android.widget.EditText').send_keys('1111')

#
# def check_cancelBtn():
#     print("check_cancelBtn")
#     try:
#         cancleBtn = driver.find_element_by_id('android:id/button2')
#     except NoSuchElementException:
#         print("No cancelBtn")
#     else:
#         cancleBtn.click()
#
#
# def check_skipBtn():
#     print("check_skinBtn")
#     try:
#         SkinBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
#     except NoSuchElementException:
#         print('No SkinBtn')
#     else:
#         SkinBtn.click()
#
#
# check_cancelBtn()
# check_skipBtn()
