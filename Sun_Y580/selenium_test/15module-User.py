from time import ctime,sleep
class Mail:
	def __init__(self,driver):
		self.driver=driver
	def login(self,username,password):
        #"""登陆""" 
		login_frame=self.driver.find_element_by_css_selector('[id^=x-URS-iframe]')
		sleep(1)
		self.driver.switch_to_frame(login_frame)  #需先跳转到iframe框架
		#self.driver.switch_to.frame('x-URS-iframe') 
		self.driver.find_element_by_name('email').clear()
		self.driver.find_element_by_name('email').send_keys('username')
		self.driver.find_element_by_name('password').clear()
		self.driver.find_element_by_name('password').send_keys('password')
		self.driver.find_element_by_id('dologin').click()

		#退出
	#driver.find_element_by_link_text("退出").click()
	def logout(self):
		"""退出"""
		self.driver.find_element_by_link_text("退出").click()
		self.driver.quit()