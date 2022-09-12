from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
link=driver.find_element_by_link_text('设置').click()
driver.find_element_by_link_text('搜索设置').click()

#保存设置条件
driver.find_element_by_class_name('prefpanelgo').click()
#driver.find_element(By.class_name,'prefpanelgo')
#获取提示框
alert=driver.switch_to.alert

alert_text=alert.alert_text
print(alert_text)