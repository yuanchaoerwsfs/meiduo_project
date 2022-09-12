import unittest
from time import sleep
import logging
from common.mult_desired_sync import appium_desired
from common.common_fun import Common


devices_list = ['127.0.0.1:62001', '127.0.0.1:62025']


class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('======setUp======')
        host = '127.0.0.1'
        port = 4723
        Common.start_devices_action(host,port)
        self.driver = appium_desired(devices_list[0],port)

    def tearDown(self):
        logging.info('=======tearDown=======')
        sleep(5)
        self.driver.close_app()
