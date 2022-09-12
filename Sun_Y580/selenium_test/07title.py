from time import sleep
from selenium.webdriver.common.keys import Keys  ###Keys   K一定要大写，大写 大写
from selenium import webdriver 
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.baidu.com/D')
print('='*50+'Before search'+'='*50)
#打印当前页面title
title=driver.title
print('title:%r'%title)
#打印当前页面URL
now_url=driver.current_url
print('now_url:%r'%now_url)

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').send_keys(Keys.ENTER)

print('='*50+'After search'+'='*50)
#再次打印当前页面title
title=driver.title
print('title:'+title)
#再次打印当前页面URL
now_url=driver.current_url
print('now_url:'+now_url)
#打印当前搜索条数
#num=driver.find_element(By.CLASS_NAME,"nums_text").text
num=driver.find_element(By.CLASS_NAME,"nums").text
#num=driver.find_element_by_class_name('/html/body/div/div[5]/div/div[2]/div/div[2]/div/span').text
print('reault:'+num)




sleep(10)
driver.quit()