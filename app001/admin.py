# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import ProductType,ProductInfo

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['typeId','name']
    # fields = ('typeId', 'name')  #显示可编辑的字段，但是会把create_date 报错
    ordering = ('typeId',)

@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    def upload_img(self, obj):
        try:
            img = mark_safe('''<a href="%s"><img src="%s" width="50px" /></a>''' % (obj.productImage.url, obj.productImage.url))
        except Exception as e:
            img = ''
        return img

    upload_img.short_description = '图片'
    upload_img.allow_tags = True
    list_display = ['productId','name','typeId','costPrice','salePrice', 'upload_img']
    readonly_fields = ['upload_img']
    # fields = ('productId', 'name', 'typeId', 'costPrice','salePrice',) #显示可编辑的字段，但是会把create_date 报错
    ordering = ('typeId',)