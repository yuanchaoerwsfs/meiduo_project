from appium_android.kyb.config import driver
from appium_android.kyb.kyb_def import *

check_cancelBtn()
check_skipBtn()
# uiautomatorID定位
# driver.find_element_by_android_uiautomator\
#     ('new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")').send_keys('yuanchaoer')
# uiautomator  TEXT定位
# driver.find_element_by_android_uiautomator\
#     ('new UiSelector().text("请输入用户名")').send_keys('yuanchaoer')
# uiautomator  CLASS定位
driver.find_element_by_android_uiautomator\
    ('new UiSelector().className("android.widget.EditText")').send_keys('yuanchaoer')




driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_password_edittext")').send_keys('qq123456')

driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_login_btn")').click()