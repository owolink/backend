
from django.db import models
from category.models import Category

class Sales(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    category = models.ManyToManyField(verbose_name='Категория', to=Category, related_name='sales')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'