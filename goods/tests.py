from django.test import testcases
import os
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','wqmproject.settings')

import django
django.setup()
from goods.models import ProductInfo
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from goods.serializers import ProductInfoSerializer


def generateGoodsData(count):
    for i in range(1,count):
        info = ProductInfo(name='我是测试'+str(i),code='10000'+ str(i),costPrice=12.09876,salePrice=32.091)
        serializer = ProductInfoSerializer(info)
        print(serializer.data)
        info.save()

def clearGoodsData():
    ProductInfo.objects.all().delete()

if __name__=='__main__':
    clearGoodsData()
    generateGoodsData(10)
    # pass
