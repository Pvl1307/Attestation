from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

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
    list_display = ('pk', 'name', 'contacts', 'get_supplier', 'debt_to_supplier', 'creation_date',)
    list_filter = ('contacts__city',)
    actions = ('clear_the_debt',)
    list_display_links = ('get_supplier',)

    def get_supplier(self, obj):
        supplier = obj.supplier
        if supplier:
            url = reverse('admin:suppliers_network_change', args=[supplier.id])
            return format_html('<a href="{}">{}</a>', url, supplier.name)
        return '-'

    get_supplier.short_description = 'Поставщик'

    @admin.action(description='Обнулить задолжность')
    def clear_the_debt(self, _, queryset):
        queryset.update(debt_to_supplier=0.00)
