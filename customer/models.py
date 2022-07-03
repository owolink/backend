from django.db import models



class Customer(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    country = models.CharField(verbose_name='Страна производства', max_length=255)

    photo = models.ImageField(verbose_name='Логотип', upload_to='customers')

    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'