# Generated by Django 4.0.5 on 2022-06-29 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('category', models.CharField(max_length=255, verbose_name='Категория')),
                ('photo', models.ImageField(upload_to='recipe', verbose_name='Фото')),
                ('product', models.CharField(max_length=255, verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
