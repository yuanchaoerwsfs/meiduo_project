import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import yagmail


# 把测试报告发到指定的邮箱
def send_mail(report):
    yag = yagmail.SMTP(user='yuanchaoer@126.com', password='qq123456', host='smtp.126.com')
    subject = '主题，自动化测试报告'
    contents = '正文，请查看附件'
    yag.send('sunqw@cashwaytech.com', subject, contents, report)
    print('email has send out !')


# 定义测试案例的目录为当前目录中的/test_case/目录
test_dir = 'D:/Sun/unittest_sample/test_case'
suit = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(suits)
    # 去当时时间作为生成报告的名称
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    html_report = 'D:/Sun/unittest_sample/test_report/' + now_time + 'result.html'
    fp = open(html_report, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            verbosity=2,
                            title="加减乘除运算/计算某年是否为闰年",
                            description='运行环境：windows 10,Chrome 浏览器')
    runner.run(suit)
    fp.close()
    send_mail(html_report)  # 发送测试报告
