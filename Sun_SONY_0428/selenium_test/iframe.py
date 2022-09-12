from time import sleep,ctime
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.126.com')
sleep(2)
driver.find_element_by_id('lbNormal').click()
print(ctime())
sleep(2)
print(ctime())

login_frame=driver.find_element_by_css_selector('[id^="x-URS-iframe"]')
#login_frame=driver.find_element_by_id('loginDiv')
#
driver.switch_to.frame(login_frame)

driver.find_element_by_name('email').send_keys('yuanchaoer')
driver.find_element_by_name('password').send_keys('jia24542')
sleep(2)
driver.find_element_by_id('dologin').click()
#driver.find_element_by_css_selector('[di="dologin"]').click()

driver.switch_to.default_content()

sleep(20)
driver.quit()