from django.urls import path
from rest_framework.routers import DefaultRouter

from suppliers.apps import SuppliersConfig
from suppliers.views import ContactsViewSet, ProductViewSet, NetworkCreateAPIView, NetworkListAPIView, \
    NetworkRetrieveAPIView, NetworkUpdateAPIView, NetworkDestroyAPIView

app_name = SuppliersConfig.name

router = DefaultRouter()
router.register(r'contacts', ContactsViewSet, basename='contacts')
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('network/create/', NetworkCreateAPIView.as_view(), name='network_create'),
    path('network/', NetworkListAPIView.as_view(), name='network_list'),
    path('network/<int:pk>/', NetworkRetrieveAPIView.as_view(), name='network_retrieve'),
    path('network/update/<int:pk>/', NetworkUpdateAPIView.as_view(), name='network_update'),
    path('network/delete/<int:pk>/', NetworkDestroyAPIView.as_view(), name='network_destroy'),
] + router.urls
