from django.shortcuts import render, redirect
from django.views import View
from django import http
import re
from django.db import DatabaseError
from .models import User
from django.urls import reverse
from django.contrib.auth import login
from meiduo_mall.utils.response_code import RETCODE


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
        return redirect(reverse('contents:index'))
