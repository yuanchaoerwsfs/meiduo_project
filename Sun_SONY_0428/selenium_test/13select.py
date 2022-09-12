from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')

link=driver.find_element_by_link_text('设置').click()
driver.find_element_by_link_text('搜索设置').click()
sleep(3)
#获取目前显示条数
sel=driver.find_element_by_name('NR')
sel2=driver.find_element_by_id('nr')
#修改显示条数为20
Select(sel).select_by_value('20')
sleep(5)
#修改显示条数为50
Select(sel2).select_by_value('50')
sleep(3)
#根据下拉选项索引修改显示条数
Select(sel).select_by_index(0)
