from rest_framework import serializers

from product.models import Product, ProductImage


class ProductImageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ('image',)


class ProductListSerializer(serializers.HyperlinkedModelSerializer):
    posted_by = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    product_image = ProductImageListSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'url',
            'uid',
            'posted_by',
            'title',
            'category',
            'price',
            'discount_price',
            'description',
            'review',
            'is_feature',
            'product_image',
        )
        extra_kwargs = {
            'url': {'view_name': 'product:product_detail', 'lookup_field': 'uid'},
        }
