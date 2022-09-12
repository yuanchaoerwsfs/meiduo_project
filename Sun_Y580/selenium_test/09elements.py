from selenium import webdriver
from time import sleep,ctime

driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
print(ctime())
sleep(5)
print(ctime())

texts=driver.find_elements_by_xpath("//div[@tpl='se_com_default']/h3/a")
print(len(texts))
for t in texts:
	print(t.text)



driver.quit()