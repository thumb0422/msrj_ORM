from django.db import models
from django.utils import timezone

# Create your models here.
# 用来保存上传图片相关信息的模型
class Profile(models.Model):
    name = models.CharField(max_length = 50,verbose_name='名称')
    # upload_to 表示图像保存路径
    picture = models.ImageField(upload_to = 'test_pictures',verbose_name='上传图片')

    class Meta:
        db_table = "profile"
        verbose_name = "图片"
        verbose_name_plural = "图片管理"

    def __str__(self):
        return self.name