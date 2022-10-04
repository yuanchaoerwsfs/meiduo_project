from yuntongxun.example.SendMessage import CCP
from . import constants
from meiduo_mall.celery_tasks.main import celery_app


@celery_app.task(name='ccp_send_sms_code')
def ccp_send_sms_code(mobile, sms_code):

        result = CCP().send_template_sms(constants.SEND_SMS_TEMPLATE_ID, mobile, (sms_code, 5))

        return result
