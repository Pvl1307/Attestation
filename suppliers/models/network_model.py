from django.db import models

from suppliers.models.contacts_model import Contacts
from suppliers.models.product_model import Product

NULLABLE = {'null': True, 'blank': True}


class Network(models.Model):
    """Модель звена сети"""
    NAMES = (
        ('Factory', 'Factory'),
        ('RN', 'Retail network'),
        ('IE', 'Individual entrepreneur')
    )

    name = models.CharField(max_length=50, choices=NAMES, verbose_name='Название звена сети')

    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, verbose_name='Контакты звена сети')
    product = models.ManyToManyField(Product, verbose_name='Продукты звена сети')

    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Поставщик звена сети', **NULLABLE)
    debt_to_supplier = models.FloatField(default=0, verbose_name='Задолженность перед поставщиком(до копеек)')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.name}, {self.supplier}'

    class Meta:
        verbose_name = 'Звено сети'
        verbose_name_plural = 'Звенья сети'
