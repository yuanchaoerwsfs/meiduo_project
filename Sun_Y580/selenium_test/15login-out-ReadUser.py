from time import ctime,sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from module import Mail

driver=webdriver.Chrome()
driver.get('http://www.126.com/')
driver.maximize_window()
sleep(1)
driver.find_element_by_id('lbNormal').click()
mail=Mail(driver)
with(open("d:/user_info.txt",'r'))as user_file:
	date=user_file.readlines()
users=[]
for line in date:
	user=line[:-1].split(':')
	users.append(user)
print(users)
sleep(1)
#登陆
#用户为空
mail.login(users[0][0],users[0][1])
sleep(2)
#密码为空
mail.login(users[1][0],users[1][1])
sleep(2)
#用户/密码错误
mail.login(users[2][0],users[2][1])
sleep(2)
#管理员登陆
mail.login(users[3][0],users[3][1])
sleep(2)
#账户密码正确
mail.login(users[4][0],users[4][1])
sleep(3)
#退出
mail.logout()
driver.quit()