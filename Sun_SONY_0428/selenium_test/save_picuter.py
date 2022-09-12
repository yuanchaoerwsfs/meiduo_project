from selenium import webdriver


driver=webdriver.Chrome()
driver.get('https://www.baidu.com/')

#截图
driver.save_screenshot('D:/baidu_img.png')   #路径必须使用‘/’
