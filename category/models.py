
from django.db import models


from product.models import Product

class Category(models.Model):
    title = models.CharField(verbose_name= '', max_length=255)
    country = models.CharField(verbose_name='Страна производства', max_length=255)
    photo = models.ImageField(verbose_name='Фото', upload_to='category')
    product = models.ManyToManyField(verbose_name='Продукт', to=Product, related_name='category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'