from django.views import View
from verifications.libs.captcha.captcha import captcha
from django import http
from django_redis import get_redis_connection
from . import constants


class ImageCodeView(View):
    def get(self, request, uuid):
        '''
        :param request: 请求对象
        :param uuid: 唯一标识图形验证码所属于的用户
        :return: image/jpg
        '''

        # 生成二维码
        text, image = captcha.generate_captcha()

        # 保存图片验证码
        redis_conn = get_redis_connection('verify_code')
        redis_conn.setex('img_%s' % uuid, constants.IMAGE_CODE_REDIS_EXPIRES, text)  # key===>uuid、redis延迟时间、value

        # 响应图片验证码
        return http.HttpResponse(image, content_type='image/jpg')  # 参数为数据、数据类型
