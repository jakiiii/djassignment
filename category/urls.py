from django.urls import path, include
from rest_framework.routers import DefaultRouter

from category.views import AdminCategoryViewSet

app_name = "categories"
categories_router = DefaultRouter()

categories_router.register('category', AdminCategoryViewSet, basename='category')


urlpatterns = [
    path('', include(categories_router.urls)),
]
