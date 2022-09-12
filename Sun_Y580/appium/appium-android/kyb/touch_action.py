from config_touch_action import driver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from time import sleep


def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


l = get_size()
print(l)


def swipeLeft():
    x1 = int(l[0] * 0.9)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.1)
    driver.swipe(x1, y1, x2, y1, 1000)


def swipeRight():
    x1 = int(l[0] * 0.9)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.1)
    driver.swipe(x2, y1, x1, y1, 1000)


def swipeDown():
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.1)
    y2 = int(l[0] * 0.9)
    driver.swipe(x1, y1, x1, y2, 1000)


def swipeUp():
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.1)
    y2 = int(l[0] * 0.9)
    driver.swipe(x1, y2, x1, y1, 1000)


# 等待页面元素加载完成后获取指定元素
WebDriverWait(driver, 15).until(lambda x: x.find_element_by_id('com.mymoney:id/next_btn'))
# 向右滑动两次
for i in range(2):
    swipeLeft()
    sleep(0.3)
# 等待页面加载
WebDriverWait(driver,5).until(lambda x: x.find_element_by_id('com.mymoney:id/begin_btn'))
driver.find_element_by_id('com.mymoney:id/begin_btn').click()
driver.implicitly_wait(3)
# 加载更多按钮并点击

WebDriverWait(driver,5).until(lambda x: x.find_element_by_id('com.mymoney:id/nav_setting_btn'))
driver.find_element_by_id('com.mymoney:id/nav_setting_btn').click()
driver.implicitly_wait(3)

for i in range(2):
    swipeUp()
    sleep(0.3)

driver.find_element_by_xpath('//*[@class="android.widget.TextView" and @text="高级"]').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@class="android.widget.TextView" and @text="密码与手势密码"]').click()
driver.implicitly_wait(3)
driver.find_elements_by_id('com.mymoney:id/switch_iv')[1].click()
driver.implicitly_wait(3)
driver.find_element_by_id('com.mymoney:id/lock_pattern_lpv').click()
driver.implicitly_wait(3)

for i in range(2):
    TouchAction(driver).press(x=212, y=291).wait(2000) \
        .move_to(x=356, y=284).wait(1000) \
        .move_to(x=505, y=430).wait(1000) \
        .move_to(x=500, y=589).wait(1000) \
        .release().perform()
