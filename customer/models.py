from django.db import models

from category.models import Category
from product.models import Product

class Customer(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    country = models.CharField(verbose_name='Страна производства', max_length=255)
    category = models.ManyToManyField(verbose_name='Категория', to=Category, related_name='customer')
    photo = models.ImageField(verbose_name='Логотип', upload_to='customers')
    product = models.ManyToManyField(verbose_name='Продукт', to=Product, related_name='customer')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'