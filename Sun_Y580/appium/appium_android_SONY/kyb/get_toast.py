# coding=utf-8   #代码中使用中文需要规定UTF-8格式
from appium_android_SONY.kyb.config import driver
from selenium.webdriver.support.ui import WebDriverWait
from appium_android_SONY.kyb.kyb_def import *

check_cancelBtn()
check_skipBtn()

driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('yuanchaoer')

driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('zxw2018')
driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
driver.get_screenshot_as_file('D:\login_2.png')
error_message = "用户名或密码错误，你还可以尝试2次"
# error_message = '账户不存在'
limit_message = "验证失败次数过多，请15分钟后再试"

message = '//*[@text=\'{}\']'.format(error_message)
# message = '//*[@text=\'{}\']'.format(limit_message)
driver.save_screenshot('login_1.png')

toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))   #无匹配信息时返回超时错误
print(toast_element.text)
