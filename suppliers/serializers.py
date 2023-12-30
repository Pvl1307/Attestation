from rest_framework import serializers

from suppliers.models import Contacts, Product, Network
from suppliers.validators import forbidden_change_debt


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = '__all__'

    def validate(self, attrs):
        instance = self.instance

        old_debt = instance.debt_to_supplier if instance else None
        new_debt = attrs.get('debt_to_supplier', old_debt)

        forbidden_change_debt(new_debt, old_debt)
        return attrs
