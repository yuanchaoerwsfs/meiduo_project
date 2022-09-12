from  time import ctime,sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException

driver=webdriver.Chrome()
driver.get('https://www.helloweba.net/demo/2017/unlock/')
sleep(2)
slider=driver.find_elements_by_calss_name('slide-to-unlock-bg')

action=ActionChains(driver)
action.click_and_hold(slider).perform()


for index in range(200):
	try:
		action.move_by_offset(2,0).perform()
	except UnexpectedAlertPresentException:
		break
	action.reset_action()
	sleep(0.1)
#打印警告框提示

success_text=driver.switch_to.alert.success_text
print(success_text)