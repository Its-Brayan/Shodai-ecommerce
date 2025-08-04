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
    ProductNumber = models.IntegerField(default=0,null=True, blank=True)
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    productStatus = models.TextField(max_length=10)
class Customers(models.Model):
    customerName = models.CharField(max_length=100)
    customerEmail = models.CharField(max_length=50, unique=True)
    customerLocation = models.CharField(max_length=50)
    customerOrders = models.IntegerField(default=0, null=True, blank=True)
    cashSpent = models.CharField(max_length=100)
class Orders(models.Model):
    OrderId = models.CharField(max_length=50)
    OrderNumber = models.IntegerField(default=0,null=True,blank=True)
    CustomerName = models.ForeignKey(Customers,on_delete=models.CASCADE)
    datePurchased = models.DateTimeField()
    paymentMethod = models.CharField(max_length=50)
    amountPaid = models.FloatField(default=0,null=True,blank=True)
    
# Create your models here.
