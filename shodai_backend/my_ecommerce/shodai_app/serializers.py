from .models import *
from rest_framework import serializers
from django.contrib.auth import get_user_model
user = get_user_model()
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
class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields ='__all__'
        extra_kwargs={
            'password':{'write_only':True},
        }
    def validate(self, data):
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError("Passwords don't Match!")
            return data
    def create(self,validated_data):
            validated_data.pop('confirm_password')
            password = validated_data.pop('password')
            user = CustomUser(**validated_data)
            user.set_password(password)
            user.save()
            return user
class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id', 'email', 'fullname', 'date_joined')