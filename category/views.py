from rest_framework.response import Response
from rest_framework import generics, mixins, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsAdmin

from category.models import Category

from category.serializers import AdminCategoriesListSerializer, AdminCategoriesCreateSerializer
from product.serializers import ProductCreateSerializer


class AdminCategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    lookup_field = 'uid'

    def get_serializer_class(self):
        if self.action in ['create', 'partial_update']:
            return AdminCategoriesCreateSerializer
        return AdminCategoriesListSerializer
