from django.contrib import admin

from suppliers.models.contacts_model import Contacts
from suppliers.models.network_model import Network
from suppliers.models.product_model import Product


@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'country', 'city', 'street', 'house_number',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'model', 'release_date',)


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'contacts', 'supplier', 'debt_to_supplier', 'creation_date',)
    list_filter = ('contacts__city',)
    actions = ('clear_the_debt',)

    @admin.action(description='Обнулить задолжность')
    def clear_the_debt(self, _, queryset):
        queryset.update(debt_to_supplier=0.00)
