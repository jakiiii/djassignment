from rest_framework import serializers

from category.models import Category


class AdminCategoriesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'name',
            'status'
        )


class AdminCategoriesCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
