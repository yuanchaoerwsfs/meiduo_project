from selenium import webdriver
from time import sleep, ctime

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

# 获取当前Cookie
cookie = driver.get_cookies()
print(cookie)

sleep(2)
# 添加cookie
driver.add_cookie({'name': 'Key-sun', 'value': 'value-sun'})

for cookie in driver.get_cookies():
    print('%s->%s' % (cookie['name'], cookie['value']))
