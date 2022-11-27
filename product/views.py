from rest_framework.response import Response
from rest_framework import generics, mixins, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from product.models import Product
from product.serializers import ProductListSerializer, ProductCreateSerializer


class ProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    lookup_field = 'uid'

    def get_serializer_class(self):
        if self.action in ['create', 'partial_update']:
            return ProductCreateSerializer
        return ProductListSerializer
