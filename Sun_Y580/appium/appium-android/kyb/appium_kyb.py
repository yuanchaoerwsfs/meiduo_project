from kyb_def import *
from kyb_register import kyb_register
from swipe import *
from time import sleep

check_cancelBtn()

for i in range(2):
    swipeLeft()
    sleep(0.3)

driver.find_element_by_id('com.tal.kaoyan:id/activity_splash_guidfinish')

for i in range(2):
    swipeRight()
    sleep(0.3)

check_skipBtn()
kyb_login()

driver.find_element_by_id('com.tal.kaoyan:id/task_no_task').click()

for i in range(2):
    swipeDown()
    sleep(0.3)
for i in  range(2):
    swipeUp()
    sleep(0.3)