from selenium import webdriver

from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)     #Keys.BACK_SPACE K区分大小写,Keys后面必须全部大写,删除一个字母
driver.find_element_by_id('kw').send_keys('m')
driver.find_element_by_id('kw').send_keys(Keys.SPACE)   #添加一个空格
driver.find_element_by_id('kw').send_keys('教程')

driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')  #全选，‘a’必须小写
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x') 
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
driver.find_element_by_id('kw').send_keys(Keys.ENTER) 

