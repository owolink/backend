
from django.db import models


class Product(models.Model):
    title = models.CharField(verbose_name='Наименование', max_length=255)
    photo = models.ImageField(verbose_name='Фото', upload_to='products')
    description = models.TextField(verbose_name='Описание')
    ingridients = models.TextField(verbose_name='Состав')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'