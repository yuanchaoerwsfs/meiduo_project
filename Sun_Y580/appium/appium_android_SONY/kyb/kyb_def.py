from appium import webdriver
from appium_android_SONY.kyb.config import *
from selenium.common.exceptions import NoSuchElementException


def check_cancelBtn():
    print("check_cancelBtn")
    try:
        cancleBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print("No cancelBtn")
    else:
        cancleBtn.click()
        driver.implicitly_wait(3)


def check_skipBtn():
    print("check_skinBtn")
    try:
        SkinBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('No SkinBtn')
    else:
        SkinBtn.click()
        driver.implicitly_wait(3)


def login():
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
    # driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('yuanchaoer')   #ID定位元素
    # #xpath相对路径定位元素
    # driver.find_element_by_xpath('//android.widget.EditText[@text="请输入用户名"]').send_keys('yuanchaoer')
    driver.find_element_by_xpath('//*[@class="android.widget.EditText" and @text="请输入用户名"]').send_keys(
        'yuanchaoer')  # xpath相对路径定位元素

    #   driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('qq123456')  #ID定位元素
    driver.find_element_by_xpath('//*[@class="android.widget.EditText" and @index="3"]').send_keys(
        'qq123456')  # xpath相对路径定位元素
    driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()
    try:
        driver.find_element_by_id('com.tal.kaoyan:id/task_no_task')
    except NoSuchElementException:
        driver.find_element_by_id('com.tal.kaoyan:id/task_no_task').click()
        driver.implicitly_wait(1)
    else:
        driver.implicitly_wait(1)



def kyb_login():
    try:
        driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl')
    except NoSuchElementException:
        login()
    else:
        driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
        driver.implicitly_wait(3)
        driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_userheader').click()
        driver.implicitly_wait(3)


def quit_login():
    try:
        driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext')
    except NoSuchElementException:
        driver.find_element_by_xpath('//*[@class="android.widget.ImageView" and @index="0"]').click()
        driver.implicitly_wait(3)
        driver.find_element_by_id('com.tal.kaoyan:id/myapptitle_RightButton_textview').click()
        driver.implicitly_wait(3)
        driver.find_element_by_id('com.tal.kaoyan:id/setting_logout_text').click()
        driver.implicitly_wait(3)
        driver.find_element_by_id('com.tal.kaoyan:id/tip_commit').click()
        driver.implicitly_wait(3)
        driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_userheader').click()
        driver.implicitly_wait(3)
        login()
    else:
        login()
