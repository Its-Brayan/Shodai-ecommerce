from django.db import models
class Category(models.Model):
    categoryImage = models.ImageField(upload_to='categories/')
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.TextField(max_length=10)
class Product(models.Model):
    productImage = models.ImageField(upload_to='products/')
    productName = models.CharField(max_length=100)
    ProductSku = models.CharField(max_length=50, unique=True)
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    productStatus = models.BooleanField(default=True)

# Create your models here.
