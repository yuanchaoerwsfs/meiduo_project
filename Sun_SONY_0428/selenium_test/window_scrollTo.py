from time import sleep
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')

driver.set_window_size(800,600)
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()

sleep(2)
#设置滚动条
js="window.scrollTo(110,850);"
sleep(2)
driver.execute_script(js)