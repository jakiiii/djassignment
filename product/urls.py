from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet

app_name = "product"
product_router = DefaultRouter()

product_router.register('product', ProductViewSet, basename='product')


urlpatterns = [
    path('', include(product_router.urls)),
]
