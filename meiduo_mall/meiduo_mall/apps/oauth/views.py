from django.shortcuts import render, redirect, reverse
from django.views import View
from django.conf import settings
from django.contrib.auth import login
from django import http
import logging, re
from django_redis import get_redis_connection

from QQLoginTool.QQtool import OAuthQQ

from utils.response_code import RETCODE
from .utils import generate_eccess_token
from .models import OAuthQQUser
from users.models import User

logger = logging.getLogger('django')  # 创建日志数据器


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

    # 提交绑定用户表单
    def post(self, request):
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        sms_code_client = request.POST.get('sms_code')
        access_token = request.POST.get('access_token')
        # 后端校验用户名和密码格式
        if not re.match('^1[3-9]\d{9}$', mobile):
            return http.HttpResponseForbidden('请输入正确的手机号码')
        if not re.match(r'^[A-Za-z0-9]{8,20}$', password):
            return http.HttpResponseForbidden('请输入8-20位的密码')
        redis_conn = get_redis_connection('verify_code')  # 连接redis数据库
        sms_code_server = redis_conn.get('sms_%s' % mobile)
        if sms_code_client != sms_code_server.decode():
            return render(request, 'oauth_callback.html', {'sms_code_errmsg': '输入短信验证码有误'})
        if sms_code_client is None:
            return render(request, 'oauth_callback.html', {'sms_code_errmsg': '无效的短信验证码'})
        if access_token is None:
            return render(request, 'oauth_callback.html', {'openid_errmsg': 'openid已经失效！'})
        # 判断access_token是否绑定用户
        try:
            user = User.objects.get(mobile=mobile)  # 判断手机号是否注册
        except User.DoesNotExist:
            user = User.objects.create_user(username=mobile, password=password, mobile=mobile)
        else:
            if not user.check_password(password):
                return render(request, 'oauth_callback.html', {'account_errmsg': '您输入的账户或者密码有误！'})

        # 将用户绑定openid
        try:
            OAuthQQUser.object.create(openid=access_token, user=user)
        except Exception as e:
            logger.error(e)
            return render(request, 'oauth_callback.html', {'qq_login_errmsg': '账号或密码错误'})
        # 实现状态保持
        login(request, user)

        # 响应绑定结果
        next = request.GET.get('state')
        response = redirect(next)

        # 登录时用户名写入到cookie，有效期15天
        response.set_cookie('username', user.username, max_age=3600 * 24 * 15)

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
