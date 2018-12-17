from django.test import testcases
import os
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','wqmproject.settings')

import django
django.setup()
from goods.models import ProductInfo

def generateGoodsData(count):
    for i in range(1,count):
        info = ProductInfo(name='我是测试'+str(i),costPrice=12.09876,salePrice=32.091)
        info.save()

def clearGoodsData():
    ProductInfo.objects.all().delete()

if __name__=='__main__':
    # generateGoodsData(10)
    # clearGoodsData()
    pass
