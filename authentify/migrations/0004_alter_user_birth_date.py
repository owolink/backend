# Generated by Django 4.0.5 on 2022-06-29 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentify', '0003_alter_user_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(verbose_name='Дата Рождения'),
        ),
    ]
