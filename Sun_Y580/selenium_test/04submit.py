from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')

#search_text=driver.find_element_by_name('wd')
size=driver.find_element_by_name('wd').size
print(size)
#search_text.send_keys('selenium')
#search_text.submit()
text=driver.find_element_by_id("cp").text
print(text)
text1=driver.find_element_by_id("jgwab").text
print(text1)
print('='*50)
text2=driver.find_element_by_xpath("/html/body/div/div[4]/div/div/p[2]").text
print(text2)
text3=driver.find_element_by_xpath("//p[@id='cp']").text
print('text3=%s'%text3)
text4=driver.find_element_by_xpath("//*[@id='cp']").text
print('text4=%s'%text4)
text5=driver.find_element_by_css_selector("#cp").text
print('text5=%s'%text5)
text6=driver.find_element_by_css_selector('#jgwab').text
print('text6=%s'%text6)