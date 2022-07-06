from rest_framework import serializers

from .models import Category, Product, ProductTransaction


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductTranscationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTransaction
        fields = '__all__'