from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from suppliers.models import Contacts, Product, Network
from suppliers.serializers import ContactsSerializer, ProductSerializer, NetworkSerializer


class ContactsViewSet(ModelViewSet):
    """Эндпоинт для контактов"""
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


class ProductViewSet(ModelViewSet):
    """Эндпоинт для продуктов"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


class NetworkCreateAPIView(generics.CreateAPIView):
    serializer_class = NetworkSerializer

    def perform_create(self, serializer):
        serializer.save()


class NetworkListAPIView(generics.ListAPIView):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country']


class NetworkRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()


class NetworkUpdateAPIView(generics.UpdateAPIView):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()

    def perform_update(self, serializer):
        serializer.save()


class NetworkDestroyAPIView(generics.DestroyAPIView):
    queryset = Network.objects.all()
