from rest_framework import serializers

from product.models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ('id', 'product', 'image')


class ProductListSerializer(serializers.ModelSerializer):
    posted_by = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = (
            'uid',
            'posted_by',
            'title',
            'category',
            'price',
            'discount_price',
            'description',
            'review',
            'is_feature',
            'status',
        )


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
