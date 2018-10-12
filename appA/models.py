from django.db import models
from django.utils import timezone

# 用来保存上传图片相关信息的模型
class Photos(models.Model):
    name = models.CharField(max_length = 50,verbose_name='名称')
    # upload_to 表示图像保存路径
    image = models.ImageField(upload_to = 'appAPhoto',verbose_name='上传图片')

    class Meta:
        db_table = "photos"
        verbose_name = "图片"
        verbose_name_plural = "图片管理"

    def __str__(self):
        return self.name

class Author(models.Model):
    #作者
    name = models.CharField(max_length=30,verbose_name='姓名')#姓名
    age = models.CharField(max_length=30,verbose_name='年龄')#年龄
    phone = models.CharField(max_length=11,verbose_name='手机号')#手机号
    email = models.EmailField(verbose_name='邮箱')#邮箱
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = '作者'

class Publisher(models.Model):#出版社
    name = models.CharField(max_length=30,verbose_name='出版社')#出版社姓名
    address = models.CharField(max_length=50,verbose_name='地址')#出版社地址
    city = models.CharField(max_length=60,verbose_name='城市')#出版社城市
    state_province = models.CharField(max_length=30,verbose_name='省份')#省份
    country = models.CharField(max_length=50,verbose_name='国家')#国家
    website = models.URLField(verbose_name='官网')#官网
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'publisher'
        verbose_name = '出版社'
        verbose_name_plural = '出版社'

class Book(models.Model):#书
    name = models.CharField(max_length=60,verbose_name='书名')#书名
    author = models.ManyToManyField(Author,verbose_name='作者')#关联作者
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE,verbose_name='出版社')#关联
    publication_date = models.DateField(verbose_name='出版时间')#时间
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'book'
        verbose_name = '书名'
        verbose_name_plural = '书名'


class Hero(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="Hero/")

    class Meta:
        db_table ='hero'
