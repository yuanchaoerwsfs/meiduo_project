from time import ctime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
driver=webdriver.Firefox()
driver.get('https://www.baidu.com/')
try:
	print(ctime())
	driver.implicitly_wait(10)
	print(ctime())
	driver.find_element_by_id('kw').send_keys('selenium')
	print(ctime())
except NoSuchElementException as e:
	print(e)
finally:
	print(ctime())
	#driver.quit()