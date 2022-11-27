from django.urls import path

from category.views import CategoryViewSet, CategoryRelatedProductViewSet

app_name = "categories"


urlpatterns = [
    path('category/', CategoryViewSet.as_view(), name='category'),
    path('category/products/', CategoryRelatedProductViewSet.as_view(), name='category_products'),
]
