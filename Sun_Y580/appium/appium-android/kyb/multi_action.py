from config_multi_action import driver
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

WebDriverWait(driver, 8).until(lambda x: x.find_element_by_id('com.baidu.BaiduMap:id/dj2'))
print('已完成‘进入地图’按钮加载')
driver.find_element_by_xpath('//*[@class="android.widget.TextView" and @text="进入地图"]').click()
driver.implicitly_wait(3)
driver.find_element_by_id('com.baidu.BaiduMap:id/byo').click()
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']


def pinch():
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    zoom_action = MultiAction(driver)
    action1.press(x=x * 0.2, y=y * 0.2).wait(1000).move_to(x=x * 0.4, y=y * 0.4).wait(1000).release()
    action2.press(x=x * 0.2, y=y * 0.2).wait(1000).move_to(x=x * 0.4, y=y * 0.4).wait(1000).release()
    print('start pinch...')
    zoom_action.add(action1, action2)
    zoom_action.perform()


def zoom():
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    zoom_action = MultiAction(driver)

    action1.press(x=x * 0.4, y=y * 0.4).wait(1000).move_to(x=x * 0.2, y=y * 0.2).wait(1000).release()
    action2.press(x=x * 0.6, y=y * 0.6).wait(1000).move_to(x=x * 0.8, y=y * 0.8).wait(1000).release()

    print('start zoom...')
    zoom_action.add(action1, action2)
    zoom_action.perform()


if __name__ == '__main__':
    for i in range(3):
        pinch()
        sleep(1)
    for i in range(3):
        zoom()
        sleep(1)
