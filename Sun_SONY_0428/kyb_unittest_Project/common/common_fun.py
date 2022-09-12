# encoding=utf-8
import logging
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from baseView.baseView import BaseView
from common.mult_desired_sync import appium_desired
from mult_appium_sync import appium_process
from multi_devices import desired_process
import time
import os, socket
import csv, codecs


class Common(BaseView):
    cancel_upgradeBtn = (By.ID, 'android:id/button2')
    skipBtn = (By.ID, 'com.tal.kaoyan:id/tv_skip')
    wemedia_cacel = (By.ID, 'com.tal.kaoyan:id/view_wemedia_cacel')

    def check_updateBtn(self):
        logging.info("======================check_cancelBtn=========================")
        try:
            element = self.driver.find_element(*self.cancel_upgradeBtn)
        except NoSuchElementException:
            logging.info("=========No cancelBtn========")
        else:
            logging.info('----click_cancelBtn----')
            element.click()

    def check_skipBtn(self):
        logging.info("======================check_skinBtn======================")
        try:
            element = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('=========No SkinBtn========')
        else:
            logging.info('----click_skipBtn----')
            element.click()

    def get_screenSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_screenSize()
        y1 = int(l[1] * 0.5)
        x1 = int(l[0] * 0.95)
        x2 = int(l[0] * 0.25)
        self.swipe(x1, y1, x2, y1, 1000)

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)

        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)

    def check_market_ad(self):
        '''检测登录或者注册之后的界面浮窗广告'''
        logging.info('=======check_market_ad=============')
        try:
            element = self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            pass
        else:
            logging.info('close market ad')
            element.click()

    def get_csv_data(self, csv_file, line):
        '''
        获取csv文件指定行的数据
        :param csv_file: csv文件路径
        :param line: 数据行数
        :return:
        '''
        with codecs.open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row

    def appium_start_sync(self):
        for desired in appium_process:
            desired.start()
        for desired in appium_process:
            desired.join()

    def devices_desired_sync(self):
        for desired in desired_process:
            desired.start()
        for desired in desired_process:
            desired.join()

    def check_port(self, host, port):
        '''检测端口是否被占用'''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
            s.shutdown(2)
        except OSError as msg:
            print('port %s is available!' % port)
            print(msg)
            return True
        else:
            print('port %s already be in use !' % port)
            return False

    def release_port(selef, port):
        '''释放指定的端口'''
        # 查找对应端口的PID
        cmd_find = 'netstat -aon | findstr %s' % port
        print(cmd_find)

        # 返回命令的执行结果
        relsult = os.popen(cmd_find).read()
        print(relsult)

        if str(port) and 'LISTENING' in relsult:
            # 获取端口对应的PID进程
            i = relsult.index('LISTENING')
            start = i + len('LISTENING') + 7
            end = relsult.index('\n')
            pid = relsult[start:end]

            # 关闭被占用端口的PID
            cmd_kill = 'taskkill -f -pid %s' % pid
            print(cmd_kill)
            os.popen(cmd_kill)
        else:
            print('port %s is available! ' % port)

    def start_appium_action(self, host, port):
        '''检查启动appium端口是否开启'''
        if self.check_port(host, port):
            self.appium_start_sync()
            return True
        else:
            print('appium %s start fail' % port)
            return False

    def start_devices_action(self, host, port):
        '''检查appium是否启动'''
        if self.start_appium_action(host, port):
            self.devices_desired_sync()
        else:
            self.release_port(port)
            self.appium_start_sync()


if __name__ == '__main__':
    pass
