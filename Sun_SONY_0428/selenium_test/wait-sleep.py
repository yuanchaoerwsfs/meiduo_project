from time import ctime,sleep
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('http://byr.wiki/')

print(ctime())
for i in range(10):
	try:

		el=driver.find_element_by_id('kw22')
		if el.is_displayed():
			break
	except:
		pass
	sleep(2)
else:
	print('time out')	
print(ctime())	
driver.quit()