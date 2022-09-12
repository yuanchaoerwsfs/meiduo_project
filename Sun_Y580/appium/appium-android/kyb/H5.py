from config_H5 import driver
from selenium.webdriver.support.ui import WebDriverWait

driver.find_element_by_id('com.wondershare.drfone:id/btnBackup').click()
print('back but')
WebDriverWait(driver,30).until(lambda x: x.find_element_by_id('com.wondershare.drfone:id/btnRecoverData'))
print('Next but')
driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()

WebDriverWait(driver,30).until(lambda x: x.find_element_by_class_name('android.webkit.WebView'))
print('click ')
contexts = driver.contexts
print(contexts)

print('switch conetext')
driver.switch_to.context('WEBVIEW_com.wondershare.drfone')
print('edit email')
driver.find_element_by_id('email').send_keys('yuanchaoer@126.com')
print('click sendBtn')
driver.find_element_by_class_name('btn_send').click()

driver.switch_to.context('NATIVE_APP')
driver.find_element_by_class_name('android.widget.ImageButton').click()