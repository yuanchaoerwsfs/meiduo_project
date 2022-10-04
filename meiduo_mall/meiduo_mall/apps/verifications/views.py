from django.views import View
from django import http
from django_redis import get_redis_connection
import random, json
#from meiduo_mall.celery_tasks.sms.tasks import ccp_send_sms_code

from verifications import constants
from verifications.libs.captcha.captcha import captcha
from utils.response_code import RETCODE
from verifications.libs.yuntongxun.example.SendMessage import CCP


class SMSCodeView(View):
    def get(self, request, mobile):
        # 接收参数
        uuid = request.GET.get('uuid')
        image_code_client = request.GET.get('image_code')
        # 参数校验
        if not all([image_code_client, uuid]):
            return http.HttpResponseForbidden('缺少必传参数')
        # 判断用户是否频繁发送验证码
        # 连接redis数据库
        redis_conn = get_redis_connection('verify_code')  # 连接redis数据库
        # 取手机验证码标记
        send_flag = redis_conn.get('send_flag_%s' % mobile)
        if send_flag:
            return http.JsonResponse({'code': RETCODE.THROTTLINGERR, "errmsg": "发送短信过于频繁"})
        # 提取图形验证码
        redis_conn = get_redis_connection('verify_code')  # 连接redis数据库
        # image_code_server = redis_conn.get('img_%s' % uuid)
        image_code_server = redis_conn.get('img_%s' % uuid)
        # 删除图形验证码
        redis_conn.delete('img_%s' % uuid)
        # 对比图形验证码
        image_code_server = image_code_server.decode()  # 将bytes转字符串，再比较
        if image_code_server.lower() != image_code_client.lower():  # 转小写，再比较
            return http.JsonResponse({'code': RETCODE.IMAGECODEERR, 'errmsg': '图形验证码输入有误'})
        if image_code_server is None:
            return http.JsonResponse({'code': RETCODE.IMAGECODEERR, 'errmsg': '短信验证码已失效'})
        # 生成短信验证码
        sms_code = '%06d' % random.randint(0, 999999)
        # # 保存短信验证码
        # redis_conn = get_redis_connection('verify_code')  # 连接redis数据库
        # redis_conn.setex('sms_%s' % mobile, constants.SMS_CODE_REDIS_EXPIRES, sms_code)
        # # 保存短信验证码的标记
        # redis_conn.setex('send_flag_%s' % mobile, constants.SEND_SMS_CODE_INTERVAL, 1)

        # 优化redis数据库连接 打包，使用管道一次性执行要执行的redis命令
        pl = redis_conn.pipeline()
        pl.setex('sms_%s' % mobile, constants.SMS_CODE_REDIS_EXPIRES, sms_code)
        # 保存短信验证码的标记
        pl.setex('send_flag_%s' % mobile, constants.SEND_SMS_CODE_INTERVAL, 1)
        pl.execute()
        # 发送短信验证码
        """
        发送短信验证码单例方法
        :param tid: 模板ID
        :param mobile: 手机号
        :param datas: 内容数据

        :return: 成功：0 失败：-1
        """

        result = CCP().send_template_sms(constants.SEND_SMS_TEMPLATE_ID, mobile, (sms_code, 5))
        # 使用异步方式处理发送短信步骤，生产者消费者模式
        #result = ccp_send_sms_code.delay(mobile, sms_code)
        # 响应结果
        result = json.loads(result)
        if result == 0:
            return http.JsonResponse({'code': RETCODE.OK, 'msg': '短信发送成功'})
        else:
            return http.JsonResponse({'code': RETCODE.SMSCODERR, 'msg': '短信发送失败'})


class ImageCodeView(View):
    def get(self, request, uuid):
        '''
        :param request: 请求对象
        :param uuid: 唯一标识图形验证码所属于的用户
        :return: image/jpg
        '''

        # 生成二维码
        text, image = captcha.generate_captcha()

        # 保存图片验证码===>存入redis
        redis_conn = get_redis_connection('verify_code')  # verify_code dev中配置的redis服务器库名称===>创建redis实例
        redis_conn.setex('img_%s' % uuid, constants.IMAGE_CODE_REDIS_EXPIRES,
                         text)  # key===>uuid；   constants.IMAGE_CODE_REDIS_EXPIRES==》redis延迟时间、   存放的value值

        # 响应图片验证码
        return http.HttpResponse(image, content_type='image/jpg')  # 参数为数据、数据类型
