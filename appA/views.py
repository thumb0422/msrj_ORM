# -*- coding: utf-8 -*-

from django.shortcuts import render,redirect
from .forms import PhotosForm # 上传图片的图表
from .models import Photos # 保存上传图片相关信息的模型

def index(request):
    context = {}
    return render(request, 'index.html', context)

def index_form(request):
    context = {}
    # 获取上传图片的表单，并加到 context 中，使得该表达能在前端展示
    form = PhotosForm
    context['form'] = form
    return render(request, 'index_form.html', context)

def save_photo(request):
    if request.method == "POST":
        # 接收 post 方法传回后端的数据
        MyProfileForm = PhotosForm(request.POST, request.FILES)
        # 检验表单是否通过校验
        if MyProfileForm.is_valid():
            # 构造一个 Profile 实例
            photo = Photos()
            # 获取name
            photo.name = MyProfileForm.cleaned_data["name"]
            # 获取图片
            photo.picture = MyProfileForm.cleaned_data["image"]
            # 保存
            photo.save()
        else:
            return redirect(to='index_form')
        return redirect(to='index_form')