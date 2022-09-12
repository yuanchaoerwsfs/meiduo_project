from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')
about=driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(about).perform()
ActionChains(driver).context_click(about).perform()





#driver.quit()