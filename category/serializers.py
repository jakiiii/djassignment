from rest_framework import serializers

from category.models import Category
from product.serializers import ProductListSerializer


class CategoriesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'uid',
            'name',
        )


class CategoryRelatedProduct(serializers.ModelSerializer):
    product_category = ProductListSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            'uid',
            'name',
            'product_category',
        )
