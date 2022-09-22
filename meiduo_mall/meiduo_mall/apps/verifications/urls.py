from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^/image_codes/(?P<uuid>[\w-]+)/$', views.ImageCodeView.as_view(), name='register'),
]
