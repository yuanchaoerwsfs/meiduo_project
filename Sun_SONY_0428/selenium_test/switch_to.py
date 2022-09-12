from selenium import webdriver
import time

driver=webdriver.Chrome()
#driver.implicitly_wait(10)
driver.get('https://www.baidu.com')

search_window=driver.current_window_handle
#driver.find_element_by_name('tj_login').click()
#driver.find_element_by_link_text('登陆').click()
#driver.find_element_by_link_text('立即注册').click()
