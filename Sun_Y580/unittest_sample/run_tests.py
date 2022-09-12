import unittest
from HTMLTestRunner import HTMLTestRunner
import time

# 定义测试案例的目录为当前目录中的/test_case/目录
test_dir = 'D:/python-test/unittest_sample/test_case'
suit = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(suits)
    # 去当时时间作为生成报告的名称
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    fp = open('D:/python-test/unittest_sample/test_report/' + now_time + 'result.html', 'wb')
    runner = HTMLTestRunner(stream=fp,
                            verbosity=2,
                            title="加减乘除运算/计算某年是否为闰年",
                            description='运行环境：windows 10,Chrome 浏览器')
    runner.run(suit)
    fp.close()
