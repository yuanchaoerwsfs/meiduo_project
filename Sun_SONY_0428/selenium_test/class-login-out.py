from time import ctime,sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from module import Mail

driver=webdriver.Chrome()
driver.get('http://www.126.com/')
driver.maximize_window()
sleep(1)
driver.find_element_by_id('lbNormal').click()
sleep(1)
mail=Mail(driver)
sleep(1)
#登陆
mail.login()
sleep(3)
#退出
mail.logout()
driver.quit()