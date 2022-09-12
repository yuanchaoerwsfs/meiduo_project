from mult_appium_sync import appium_process
from multi_devices import desired_process
from check_port import *
from time import sleep
import multiprocessing



def start_appium_action(host, port):
    '''检查启动appium端口是否开启'''
    if check_port(host, port):
        appium_start_sync()
        return True
    else:
        print('appium %s start fail' % port)
        return False


def start_devices_action(host, port):
    '''检查appium是否启动'''
    if start_appium_action(host, port):
        devices_desired_sync()
    else:
        release_port(port)
        appium_start_sync()


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 4723
    start_devices_action(host, port)
