from selenium import webdriver
driver=webdriver.Chrome()
driver.get('http://byr.wiki/')

driver.find_element_by_id('search').send_keys('selenium')
driver.find_element_by_id('search').clear()   #删除指定位置文本
driver.find_element_by_id('search').send_keys('atom')
driver.find_element_by_id('baidu').click()
