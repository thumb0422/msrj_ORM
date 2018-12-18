# -*- coding: utf-8 -*-
from rest_framework import serializers
from goods.models import ProductInfo

class ProductInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductInfo
        fields = ['code', 'name', 'costPrice','salePrice']