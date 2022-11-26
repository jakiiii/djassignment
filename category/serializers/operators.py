from rest_framework import serializers

from category.models import Category


class OperatorCategoriesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
            'status'
        )


class OperatorCategoriesCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
