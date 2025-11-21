from rest_framework import serializers
from .models import Category, Product


class CatergorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_image']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'price', 'owner', 'image', 'phone_number', 'description', 'product_type', 'created_date']










