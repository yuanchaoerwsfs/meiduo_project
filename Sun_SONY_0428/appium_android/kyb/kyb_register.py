from appium_android.kyb.config import driver
from selenium.common.exceptions import NoSuchElementException
import random


def register():
    driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
    driver.implicitly_wait(2)
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()
    driver.implicitly_wait(2)
    images = driver.find_elements_by_id('com.tal.kaoyan:id/item_image')
    driver.implicitly_wait(2)
    images[10].click()
    driver.implicitly_wait(2)
    driver.find_element_by_id('com.tal.kaoyan:id/save').click()
    # 填写用户名、密码、邮箱
    username = 'kybapp' + str(random.randint(1000, 9000))
    print(username)
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys(username)
    password = 'Qq1234' + str(random.randint(200, 500))
    print(password)
    driver.implicitly_wait(2)
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').click()
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys(password)
    email = '359792' + str(random.randint(100, 200)) + '@163.com'
    driver.implicitly_wait(2)
    print(email)
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').click()
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys(email)
    driver.implicitly_wait(2)
    driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()
    driver.implicitly_wait(2)


def kyb_register():
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
        register()
    else:
        register()


def register_school():
    driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_time').click() #入学时间
    driver.find_elements_by_id('android:id/text1')[4].click()                           #2020

    driver.find_elements_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name')[0].click()   #选择学院
    driver.find_elements_by_id('com.tal.kaoyan:id/more_forum_title')[2].click()                 #天津
    driver.find_elements_by_id('com.tal.kaoyan:id/university_search_item_name')[5].click()     #外国语大学

    driver.find_elements_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name')[1].click()   #选择学院
    driver.find_elements_by_id('com.tal.kaoyan:id/more_forum_title')[7].click()                 #重庆
    driver.find_elements_by_id('com.tal.kaoyan:id/university_search_item_name')[2].click()     #重庆理工

    driver.find_elements_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name')[2].click()   #选择学院
    driver.find_elements_by_id('com.tal.kaoyan:id/more_forum_title')[8].click()                 #山东
    driver.find_elements_by_id('com.tal.kaoyan:id/university_search_item_name')[1].click()  # 中国石油大学

    driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()    #专业选择
    driver.find_elements_by_id('com.tal.kaoyan:id/major_subject_title')[9].click()  # 医学
    driver.find_elements_by_id('com.tal.kaoyan:id/major_group_title')[2].click()  # 口腔医学
    driver.find_elements_by_id('com.tal.kaoyan:id/major_search_item_name')[0].click()  # 口腔医学

    driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()   #进入考研帮
    driver.find_element_by_id('com.tal.kaoyan:id/view_wemedia_cacel').click()  # 取消广告


