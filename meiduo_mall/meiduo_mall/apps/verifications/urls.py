from django.urls import re_path as url
from verifications import views

urlpatterns = [
    url(r'^image_codes/(?P<uuid>[\w-]+)/$', views.ImageCodeView.as_view()),
    url(r'^SMSCodeView/(?P<mobile>1[3-9]\d{9})/$', views.SMSCodeView.as_view()),
]
