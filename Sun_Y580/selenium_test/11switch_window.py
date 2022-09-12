from time import sleep
from selenium import webdriver

driver=webdriver.Chrome()
#driver.implicitly_wait(10)
driver.get('https://www.baidu.com/')
#获取当前窗口句柄
search_window=driver.current_window_handle
#print(search_window)
driver.find_element_by_link_text('登录').click()
sleep(1)
driver.find_element_by_link_text('立即注册').click()
#driver.find_element_by_xpath('//a[@class^="pass-reglink"]').click()
#driver.find_element_by_xpath('//html/body/div[3]/div[2]/div[2]/div/div/div/div/div[4]/div/a').click()
#获取当前所有打开窗口句柄
all_window=driver.window_handles

for handle in all_window:
	if handle!=search_window:
		driver.switch_to_window(handle)
		print(driver.title)
	else:
		print('窗口句柄一致')
driver.find_element_by_name('userName').send_keys('yuanchaoersun')
driver.find_element_by_name('phone').send_keys('13362213853')
#driver.find_element_by_link_text('请设置登录密码').send_keys('qq123456')
sleep(2)
#关闭当前窗口
driver.close()
sleep(2)
#回到搜索窗口
driver.switch_to.window(search_window)
driver.find_element_by_class_name('buttons').click()
print(driver.title)


