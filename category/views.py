from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from category.models import Category

from category.serializers import CategoriesListSerializer, CategoryRelatedProduct


class CategoryViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategoriesListSerializer
    queryset = Category.objects.all()


class CategoryRelatedProductViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategoryRelatedProduct
    queryset = Category.objects.all()
