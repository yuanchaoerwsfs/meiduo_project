from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^areas/$', views.AreasView.as_view(), name='area'),

]