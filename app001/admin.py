# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.db.models import Sum,Count,Max,Min,Avg
from .models import ProductType,ProductInfo,OrderMain,OrderDetail

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['typeId','name','isValid']
    fields = ('typeId', 'name','isValid')
    ordering = ('typeId',)

@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):

    '''create_by 修改时为当前用户'''
    def save_model(self, request, obj, form, change):
        obj.creat_by = request.user
        super().save_model(request, obj, form, change)

    '''过滤出分类isValid=True的数据'''
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "typeId":
            kwargs["queryset"] = ProductType.objects.filter(isValid=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def upload_img(self, obj):
        try:
            img = mark_safe('''<a href="%s"><img src="%s" height="30px" width="30px" /></a>''' % (obj.productImage.url, obj.productImage.url))
        except Exception as e:
            img = ''
        return img

    upload_img.short_description = '缩略图'
    upload_img.allow_tags = True
    list_display = ['productId','name','typeId','costPrice','salePrice', 'upload_img','isValid']
    readonly_fields = ['upload_img']
    fields = ('typeId', 'productId', 'name', 'costPrice','salePrice','productImage','upload_img','isValid') #显示可编辑的字段
    ordering = ('typeId',)

class OrderDetailInLine(admin.TabularInline):
    model = OrderDetail
    extra = 1

@admin.register(OrderMain)
class OrderMainAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        '''create_by 修改时为当前用户'''
        obj.creat_by = request.user
        # tt = OrderDetail.objects.filter(orderId=obj.orderId).aggregate(Sum('orderCount'))
        super().save_model(request, obj, form, change)

    def formateCreateDate(self,obj):
        return obj.create_Date.strftime('%Y/%m/%d %H:%M:%S')
    formateCreateDate.short_description = '创建时间'
    inlines = [OrderDetailInLine,]
    list_display = ['orderId','comment','formateCreateDate','isValid']
    readonly_fields = ['orderId','sumAmount']
    fields = ('orderId', 'sumAmount', 'comment', 'isValid')  # 显示可编辑的字段

