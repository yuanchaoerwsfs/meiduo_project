from django.conf import settings
from django.core.mail import send_mail
from celery_tasks.main import celery_app
import logging

# 创建日志
logger = logging.getLogger('django')


@celery_app.task(bind=True, name='send_verify_email', retry_backoff=3)
def send_verify_email(self, to_email, verify_url):  # 当bind=True时，第一个参数添加self，表示send_verify_email任务，下面可直接调用
    """
    发送验证邮箱邮件
    :param to_email: 收件人邮箱
    :param verify_url: 验证链接
    :return: None
    """
    subject = "美多商城邮箱验证"
    html_message = '<p>尊敬的用户您好！</p>' \
                   '<p>感谢您使用美多商城。</p>' \
                   '<p>您的邮箱为：%s 。请点击此链接激活您的邮箱：</p>' \
                   '<p><a href="%s">%s<a></p>' % (to_email, verify_url, verify_url)
    try:
        send_mail(subject, "", settings.EMAIL_FROM, [to_email], html_message=html_message)
    except Exception as e:
        logger.error(e)
        # 有异常自动重试三次
        raise self.retry(exc=e, max_retries=3)  # 直接调用！！！！！

"""
扩展：
启动Celery框架命令：celery -A celery_tasks.main worker -l info   默认CPU*4个进程
设置最大进程数celery -A celery_tasks.main worker -l info -c 20    # -c 20 表示最大启动20个进程    路径填写到.main；

设置协程数
pip install evenlet 
celery -A celery_tasks.main worker -l info -P evenlet -c 1000   开启1000个协程    协程占用资源小



"""



def send_verify_email_1(to_email, verify_url):  # 当bind=True时，第一个参数添加self，表示send_verify_email任务，下面可直接调用
    """
    发送验证邮箱邮件
    :param to_email: 收件人邮箱
    :param verify_url: 验证链接
    :return: None
    """
    subject = "美多商城邮箱验证"
    html_message = '<p>尊敬的用户您好！</p>' \
                   '<p>感谢您使用美多商城。</p>' \
                   '<p>您的邮箱为：%s 。请点击此链接激活您的邮箱：</p>' \
                   '<p><a href="%s">%s<a></p>' % (to_email, verify_url, verify_url)
    try:
        send_mail(subject, "", settings.EMAIL_FROM, [to_email], html_message=html_message)
    except Exception as e:
        logger.error(e)

