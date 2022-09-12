from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://m.baidu.com')
print('输出窗口为宽480*高800')
driver.set_window_size(480,800)  #窗口480*800
driver.refresh()
driver.maximize_window()  #窗口最大化

first_url='http://www.baidu.com'
print('now access %s'%first_url)
driver.get(first_url)

second_url='http://news.baidu.com'
print('now access %s'%second_url)
driver.get(second_url)

print('back to %s'%(first_url))
driver.back()

print('forward to %s'%(second_url))
driver.forward()
driver.refresh()  #浏览器刷新

print('进入http://byr.wiki/')
byr_url=("http://byr.wiki/")
driver.get(byr_url)
driver.find_element_by_name('wd').send_keys('selenium')
driver.find_element_by_id("baidu").click()












#driver.quit()