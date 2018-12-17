from django.db import models
from utility.strExtension import generate_random_str

# Create your models here.
class ProductInfo(models.Model):
    code = models.CharField(max_length=20,unique=True,default=generate_random_str(6))
    name = models.CharField(max_length=50,null=False)
    costPrice = models.DecimalField(max_digits=10,decimal_places=2)
    unit = models.CharField(max_length=10)
    salePrice = models.DecimalField(max_digits=10,decimal_places=2)

    isValid = models.BooleanField(default=True)
    create_Date = models.DateTimeField(auto_now_add=True)
    update_Date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_info'
        verbose_name = '产品信息'
        verbose_name_plural = '产品信息'
        ordering=('create_Date',)

    def __str__(self):
        return self.name