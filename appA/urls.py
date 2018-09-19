# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import save_photo,index_form,index

urlpatterns = [
    url(r'^$', index, name='index'),
    # 上传并保存图片的 url
    url(r'^save_photo/', save_photo, name='save_profile'),
    # 展示表单的 url
    url(r'^index_form/', index_form, name='index_form'),
]