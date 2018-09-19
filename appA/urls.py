# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import save_profile,index_form

urlpatterns = [
    # 上传并保存图片的 url
    url(r'^save_profile/', save_profile, name='save_profile'),
    # 展示表单的 url
    url(r'^index_form/', index_form, name='index_form'),
]