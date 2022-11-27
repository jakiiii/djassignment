from django.urls import path

from product.views import ProductListAV, ProductRetrieveAV

app_name = "product"


urlpatterns = [
    path('product/', ProductListAV.as_view(), name="product"),
    path('product/<str:uid>/', ProductRetrieveAV.as_view(), name="product_detail"),
]
