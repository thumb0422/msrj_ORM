# -*- coding: utf-8 -*-
from django.db import models

#产品分类
class ProductType(models.Model):

    typeId = models.CharField(max_length=20,blank=False,verbose_name='分类代码')
    name = models.CharField(max_length=40,blank=False,verbose_name='分类名称')
    create_Date = models.DateTimeField(auto_created=True)
    update_Date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'productType'
        verbose_name = '产品分类'
        verbose_name_plural = '产品分类'

    def __str__(self):
        return self.name

#产品详情
class ProductInfo(models.Model):

    productId = models.CharField(max_length=10,blank=False,verbose_name='产品代码')
    name = models.CharField(max_length=100, blank=False,verbose_name='产品名称')
    typeId = models.ForeignKey(ProductType,on_delete=models.DO_NOTHING,verbose_name='所属分类')
    costPrice = models.DecimalField(max_digits=10,decimal_places=3,verbose_name='成本价')
    salePrice = models.DecimalField(max_digits=10,decimal_places=3,verbose_name='销售价')
    productImage = models.ImageField(null=True, blank=True, upload_to="product/")
    create_Date = models.DateTimeField(auto_created=True)
    update_Date = models.DateTimeField(auto_now=True)
    # creat_by = models.ForeignKey() #最好是加载登录用户

    class Meta:
        db_table = 'product'
        verbose_name = '产品详情'
        verbose_name_plural = '产品详情'

    def __str__(self):
        return self.name