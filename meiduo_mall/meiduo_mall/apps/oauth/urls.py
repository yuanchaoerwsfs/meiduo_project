from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^qq/login/$', views.QQAuthURLView.as_view(), name='register'),
]