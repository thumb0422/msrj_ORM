from django.test import testcases
import os
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','wqmproject.settings')

import django
django.setup()

def generateGoodsData(count):
    from goods.models import ProductInfo
    for i in range(1,count):
        info = ProductInfo(name='我是测试'+str(i),code='1000'+str(i),costPrice=12.09876,salePrice=32.091)
        info.save()


if __name__=='__main__':
    # generateGoodsData(10)
    pass
