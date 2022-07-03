
from django.db import models

class Recipes(models.Model):
    title =  models.CharField(verbose_name= 'Название', max_length=255, )
    category =  models.CharField(verbose_name= 'Категория', max_length=255, )
    photo =  models.ImageField(verbose_name= 'Фото', upload_to= 'recipe' )
    product =  models.CharField(verbose_name= 'Продукт', max_length=255 )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
