# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import path
from goods import views,apiViews

# urlpatterns = [
#     url(r'^$', index, name='index'),
# ]


urlpatterns = [
    path('', views.goods_list),
    url(r'^api/', apiViews.api_GetList, name='api_GetList'),
    path('<int:pk>/', views.goods_detail),
]