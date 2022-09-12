from time import sleep
from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')

link=driver.find_element_by_link_text('设置').click()
driver.find_element_by_class_name('setpref').click()
#driver.find_element_by_link_text('搜索设置').click()
sleep(3)
driver.find_element_by_link_text('保存设置').click()

#获取弹框信息
alert=driver.switch_to.alert
#将获取到的信息复制给变量   直接打印alert.text也可以
alert_text=alert.text
print(alert_text)
print(alert.text)
sleep(3)
alert.accept()