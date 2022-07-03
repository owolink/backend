from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from authentify.manager import UserManager
from datetime import date


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email Адрес', max_length=255, unique=True)
    name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    birth_date = models.DateField(verbose_name='Дата Рождения', auto_now=False, auto_now_add=False, null=True, blank=False)

    is_active = models.BooleanField(verbose_name= 'Активированный пользователь', default=False)
    is_staff = models.BooleanField(verbose_name= 'Персонал', default=False)
    is_superuser = models.BooleanField(verbose_name= 'Администратор', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name', 'birth_date']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'