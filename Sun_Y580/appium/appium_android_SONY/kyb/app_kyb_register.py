from appium_android_SONY.kyb.kyb_def import *
from appium_android_SONY.kyb.kyb_register import kyb_register, register_school
from selenium.webdriver.support.ui import WebDriverWait

driver.implicitly_wait(8)
check_cancelBtn()  # 检查是否有更新界面
check_skipBtn()  # 检查是否有引导界面
# kyb_login()    #点击我的，判断是否在登陆界面登陆
# quit_login()    #退出登陆
kyb_register()  # 注册账户
register_school()  # 填写考研信息
