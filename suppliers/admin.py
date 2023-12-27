from django.contrib import admin

from suppliers.models.contacts_model import Contacts
from suppliers.models.network_model import Network
from suppliers.models.product_model import Product


@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'country', 'city', 'street', 'house_number',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'model', 'release_date',)


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'contacts', 'product', 'supplier', 'debt_to_supplier', 'creation_date',)
