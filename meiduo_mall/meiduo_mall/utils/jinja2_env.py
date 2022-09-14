from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse


def jinja2_environment(**options):
    #创建环境对象
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,    #获取静态文件的路径
        'url': reverse,    #重定向=反向解析
    })
    #返回环境对象
    return env
