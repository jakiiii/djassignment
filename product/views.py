from rest_framework.response import Response
from rest_framework import generics, mixins, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from product.models import Product
from product.serializers import ProductListSerializer


class ProductListAV(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductRetrieveAV(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    lookup_field = 'uid'
