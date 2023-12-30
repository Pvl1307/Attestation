from django.db import models


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    model = models.CharField(max_length=255, verbose_name='Модель продукта')
    release_date = models.DateField(verbose_name='Дата выхода на рынок')

    def __str__(self):
        return f'Продукт {self.name} {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
