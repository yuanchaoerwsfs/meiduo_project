from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://videojs.com/')
sleep(5)
video = driver.find_element_by_id('preview-player_html5_api')
print('Video:%s' % video)
sleep(5)
# 返回URL地址
URL = driver.execute_script('return arguments[0].currentScr;', video)
print('URL:%s' % URL)

# 播放视频
print('start')
driver.execute_script('arguments[0].play()', video)
# 播放15S
sleep(30)
print('stop')
driver.execute_script('arguments[0].pause()', video)
