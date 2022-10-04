from django.shortcuts import render,redirect,reverse
from django.views import View
from django.conf import settings
from django.contrib.auth import login
from django import http
import logging

from QQLoginTool.QQtool import OAuthQQ


from utils.response_code import RETCODE
from .utils import generate_eccess_token
from .models import OAuthQQUser

logger = logging.getLogger('django')#创建日志数据器


class QQAuthUserView(View):
    def get(self, request):
        # 第二步
        # 通过返回的通过Authorization Code获取Access Token
        # access_token = oauth.get_access_token(code)
        code = request.GET.get('code')  # 获取get中参数
        if not code:
            return http.HttpResponseForbidden('缺少code')
        oauth = OAuthQQ(client_id=settings.QQ_CLIENT_ID, client_secret=settings.QQ_CLIENT_SECRET,
                        redirect_uri=settings.QQ_REDIRECT_URI)  # 创建oauth对象
        try:
            # 使用code向QQ服务器请求access_token
            access_token = oauth.get_access_token(code)
            # 第三步
            # 通过Access Token获取OpenID
            # openid = oauth.get_open_id(access_token)
            # 使用access_token向QQ服务器请求openid
            openid = oauth.get_open_id(access_token)
        except Exception as e:
            logger.error(e)
            return http.HttpResponseServerError('OAuth2.0认证失败')
        try:
            oauth_user = OAuthQQUser.objects.get(openid=openid)
        except OAuthQQUser.DoesNotExist:
            # 如果openid没绑定美多商城用户
            access_token = generate_eccess_token(openid)
            context = {'access_token_openid': access_token}
            return render(request, 'oauth_callback.html', context)
        else:
            # 如果openid已绑定美多商城用户
            # 实现状态保持
            qq_user = oauth_user.user
            login(request, qq_user)

            # 重定向到主页
            response = redirect(reverse('contents:index'))

            # 登录时用户名写入到cookie，有效期15天
            response.set_cookie('username', qq_user.username, max_age=3600 * 24 * 15)

            return response


# 第一步
# 获取QQ二维码登录地址 login_url = oauth.get_qq_url()
class QQAuthURLView(View):
    def get(self, request):
        next = request.GET.get('next')  # 获取get中参数
        oauth = OAuthQQ(client_id=settings.QQ_CLIENT_ID, client_secret=settings.QQ_CLIENT_SECRET,
                        redirect_uri=settings.QQ_REDIRECT_URI, state=next)  # 创建oauth对象
        login_url = oauth.get_qq_url()  # 调用对象中方法
        return http.JsonResponse({'code': RETCODE.OK, 'errmsg': 'OK', 'login_url': login_url})  # 返回QQ登录二维码
