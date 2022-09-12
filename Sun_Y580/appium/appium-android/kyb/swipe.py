from config import driver
from time import sleep
#from kyb_def import check_cancelBtn

#check_cancelBtn()


def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


l = get_size()
print(l)


def swipeLeft():
    x1 = int(l[0] * 0.9)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.1)
    driver.swipe(x1, y1, x2, y1, 1000)


def swipeRight():
    x1 = int(l[0] * 0.9)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.1)
    driver.swipe(x2, y1, x1, y1, 1000)


def swipeDown():
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.1)
    y2 = int(l[0] * 0.9)
    driver.swipe(x1, y2, x1, y1, 1000)


def swipeUp():
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.1)
    y2 = int(l[0] * 0.9)
    driver.swipe(x1, y1, x1, y2, 1000)
