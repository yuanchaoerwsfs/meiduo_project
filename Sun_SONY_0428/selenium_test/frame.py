from time import ctime,sleep
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('http://www.126.com/')
driver.find_element_by_id('lbNormal').click()

login_frame=driver.find_element_by_css_selector('[id^=x-URS-iframe]')
driver.switch_to_frame(login_frame)  #需先跳转到iframe框架
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys('yuanchaoer')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('jia24542')
driver.find_element_by_id('dologin').click()
sleep(2)
#退出
driver.find_element_by_link_text("退出").click()
sleep(10)
driver.quit()