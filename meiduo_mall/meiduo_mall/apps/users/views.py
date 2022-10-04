from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django import http
from django_redis import get_redis_connection
from django.db import DatabaseError
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate

import re

from meiduo_mall.utils.response_code import RETCODE
from .models import User


class UserInfoView(LoginRequiredMixin, View):
    """
    Django用户认证系统提供了方法request.user.is_authenticated()来判断用户是否登录。如果通过登录验证则返回True。反之，返回False。
    """

    def get(self, request):
        # 方法一：
        # if request.user.is_authenticated:
        #     return render(request, 'user_center_info.html')
        # else:
        #     return render(reverse('users:login'))  # user:login===>app中模块名：命名空间
        # 方法二:
        # login_url = self.login_url or settings.LOGIN_URL   验证完成后要跳转的页面
        # login_url='/login/'   或者在setting中配置LOGIN_URL='/login/' 效果一样
        return render(request, 'user_center_info.html')


class LogoutView(View):
    def get(self, request):
        # 清理session
        logout(request)
        # 退出之后重定向登录页
        response = redirect(reverse('contents:index'))
        # 退出登录时清楚cookie中的username
        response.delete_cookie('username')

        return response  # 返回请求后前端进行session和cockie清除处理===>赋空值

    pass


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        remembered = request.POST.get('remembered')
        # 后端校验用户名和密码格式
        if not re.match(r'^[A-Za-z0-9_-]{5,20}$', username):
            return http.HttpResponseForbidden('请输入正确的账户或手机号码')
        if not re.match(r'^[A-Za-z0-9]{8,20}$', password):
            return http.HttpResponseForbidden('请输入8-20位的密码')
        # 认证登录用户
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, 'login.html', {"account_errmsg": "用户名或密码错误"})
        # 实现状态保持
        login(request, user)
        # 设置状态保持的周期
        if remembered != 'on':
            # 没有记住用户，浏览器会话结束就过去
            request.session.set_expiry(0)
        else:
            # 记录用户：none表示两周后过期
            request.session.set_expiry(None)
        next = request.GET.get('next')
        if next:
            response = redirect(next)
        else:
            response = redirect(reverse('contents:index'))
        response.set_cookie('username', user.username, max_age=3600 * 24 * 15)
        return response


class UsernameCountView(View):
    """判断用户名是否重复注册"""

    def get(self, request, username):
        count = User.objects.filter(username=username).count()
        return http.JsonResponse({'code': RETCODE.OK, 'errmsg': 'OK', 'count': count})  # 返回json格式数据


class MobileCountView(View):
    """判断手机号是否重复注册"""

    def get(self, request, mobile):
        count = User.objects.filter(mobile=mobile).count()
        return http.JsonResponse({'code': RETCODE.OK, 'errmsg': 'OK', 'count': count})  # 返回json格式数据


class RegisterView(View):
    """用户注册"""

    def get(self, request):
        """
        提供注册界面
        :param request: 请求对象
        :return: 注册界面
        """
        return render(request, 'register.html')

    def post(self, request):
        """
        实现用户注册
        :param request: 请求对象
        :return: 注册结果
        """
        # 获取请求参数
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        mobile = request.POST.get('mobile')
        allow = request.POST.get('allow')
        sms_code_client = request.POST.get('sms_code')
        # 参数的逻辑校验
        if not all([username, password, password2, mobile, allow]):
            return http.HttpResponseForbidden('缺少必输字段')
        if not re.match(r'^[A-Za-z0-9_-]{5,20}$', username):
            return http.HttpResponseForbidden('请输入5-20位的账户')
        if not re.match(r'^[A-Za-z0-9]{8,20}$', password):
            return http.HttpResponseForbidden('请输入8-20位的密码')
        if password != password2:
            return http.HttpResponseForbidden('两次密码输入的不一致')
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return http.HttpResponseForbidden('请输入正确的11位手机号码')
        if allow != 'on':
            return http.HttpResponseForbidden('请勾选注册协议')
        # 短信验证码校验
        redis_conn = get_redis_connection('verify_code')  # 连接redis数据库
        sms_code_server = redis_conn.get('sms_%s' % mobile)
        if sms_code_client != sms_code_server.decode():
            return render(request, 'register.html', {'sms_code_errmsg': '输入短信验证码有误'})
        if sms_code_client is None:
            return render(request, 'register.html', {'sms_code_errmsg': '无效的短信验证码'})

        # 保存注册数据
        try:
            user = User.objects.create_user(username=username, password=password, mobile=mobile)
        except DatabaseError:
            return render(request, 'register.html', {'register_errmsg': '注册失败'})

        # 保持登录状态
        login(request, user)
        pass
        # 响应结果
        # return http.HttpResponse('注册成功，重定向到首页')
        response = redirect(reverse('contents:index'))  # redirect(reverse('contents:index')) 返回的是response给前端渲染
        # 登录时用户名写入到cookie，有效期15天
        response.set_cookie('username', user.username, max_age=3600 * 24 * 15)

        return response
