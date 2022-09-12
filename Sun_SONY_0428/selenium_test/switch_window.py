from time import ctime,sleep
from selenium import webdriver

driver=webdriver.Chrome()
#driver.implicitly_wait(10)
driver.get('https://www.baidu.com/')
#获取当前窗口句柄
search_window=driver.current_window_handle
#print(search_window)
driver.find_element_by_link_text('登录').click()
sleep(2)
driver.find_element_by_link_text('立即注册').click()
#driver.find_element_by_xpath('//html/body/div[3]/div[2]/div[2]/div/div/div/div/div[4]/div/a').click()
#driver.find_element_by_class_name('pass-reglink').click()


#获取当前所有打开窗口句柄
all_window=driver.window_handles

for handle in all_window:
	if handle!=search_window:
		driver.switch_to_widow(handle)
		print(driver.title)
	else:
		print('窗口句柄一直')