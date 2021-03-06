# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.conf import settings
from utility import strExtension

#产品分类
class ProductType(models.Model):

    typeId = models.CharField(max_length=20,unique=True,blank=False,verbose_name='分类代码')
    name = models.CharField(max_length=40,blank=False,verbose_name='分类名称')
    isValid = models.BooleanField(default=True,verbose_name='有效')
    create_Date = models.DateTimeField(default = timezone.now)
    update_Date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'productType'
        verbose_name = '产品分类'
        verbose_name_plural = '产品分类'

    def __str__(self):
        return self.name

#产品详情
class ProductInfo(models.Model):

    def upload_location(instance, filename):
        extension = filename.split(".")[-1]
        return "{0}/{1}.{2}".format(instance._meta.app_label,strExtension.generate_random_str(12), extension)

    productId = models.CharField(unique=True,max_length=10,blank=False,verbose_name='产品代码')
    name = models.CharField(max_length=100, blank=False,verbose_name='产品名称')
    typeId = models.ForeignKey(ProductType,to_field='typeId',db_column='typeId',on_delete=models.CASCADE,verbose_name='所属分类')
    costPrice = models.DecimalField(max_digits=10,decimal_places=3,verbose_name='成本价')
    salePrice = models.DecimalField(max_digits=10,decimal_places=3,verbose_name='销售价')
    productImage = models.ImageField(null=True, blank=True, verbose_name='上传图片', upload_to=upload_location)
    isValid = models.BooleanField(default=True, verbose_name='有效')
    create_Date = models.DateTimeField(default = timezone.now)
    update_Date = models.DateTimeField(auto_now=True)
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, db_column='create_by',blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'
        verbose_name = '产品详情'
        verbose_name_plural = '产品详情'

    def __str__(self):
        return self.name


'''订单主表'''
class OrderMain(models.Model):
    def getGenerateOrderId(preStr):
        return strExtension.generate_orderId(preStr)

    orderId = models.CharField(primary_key=True, max_length=30, verbose_name='订单ID',default=getGenerateOrderId('OR'))
    sumAmount = models.DecimalField(max_digits=13,decimal_places=3,null=True,verbose_name='订单总价')
    comment = models.TextField(verbose_name='备注')
    create_Date = models.DateTimeField(default=timezone.now)
    update_Date = models.DateTimeField(auto_now=True)
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='create_by',null=True, blank=True, on_delete=models.SET_NULL)
    isValid = models.BooleanField(default=True, verbose_name='有效')

    class Meta:
        db_table = 'orderMain'
        verbose_name = '订单'
        verbose_name_plural = '订单'

    def __str__(self):
        return self.orderId

    def save(self, *args, **kwargs):
        super(OrderMain, self).save(*args, **kwargs)  # Call the "real" save() method.
        # TODO:在此处重新存储好像一直在遍历存储
        # ammount = 0
        # for item in OrderDetail.objects.filter(orderId=self.orderId):
        #     ammount += item.orderCount
        # mainOrder = OrderMain.objects.get(orderId=self.orderId)
        # mainOrder.sumAmount = ammount
        # mainOrder.save()

'''订单从表'''
class OrderDetail(models.Model):
    orderId = models.ForeignKey(OrderMain,to_field='orderId',db_column='orderId',on_delete=models.CASCADE,verbose_name='订单ID')
    productId = models.ForeignKey(ProductInfo, to_field='productId', on_delete=models.CASCADE, verbose_name='产品')
    orderCount = models.DecimalField(max_digits=8,decimal_places=2,verbose_name='数量')

    class Meta:
        db_table = 'orderDetail'
        verbose_name = '订单明细'
        verbose_name_plural = '订单明细'

    def __str__(self):
        return '' #好像不能显示为外健
