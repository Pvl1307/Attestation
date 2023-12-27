from django.db import models


class Contacts(models.Model):
    """Модуль контактов звена"""
    email = models.EmailField(verbose_name='Электронная почта')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.IntegerField(verbose_name='Номер дома')

    def __str__(self):
        return f'Контакты: {self.email}, {self.country}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
