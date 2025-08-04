from .models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    categoryName = serializers.CharField(source='productCategory.categoryName', read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'
class OrdersSerializer(serializers.ModelSerializer):
    customeremail = serializers.CharField(source='CustomerName.customerEmail', read_only=True)
    class Meta:
        model = Orders
        fields = '__all__'