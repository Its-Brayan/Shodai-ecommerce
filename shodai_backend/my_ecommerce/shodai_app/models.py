from django.db import models
from django.contrib.auth.models import AbstractUser
class Category(models.Model):
    categoryImage =  models.URLField(max_length=100000,blank=True,null=True)
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.TextField(max_length=10)
    def __str__(self):
        return f"{self.categoryName} {self.categoryDescription} {self.categoryStatus} {self.categoryImage}"
class Product(models.Model):
    productImage = models.URLField(max_length=10000,blank=True,null=True)
    productName = models.CharField(max_length=100)
    ProductSku = models.CharField(max_length=50, unique=True)
    ProductNumber = models.IntegerField(default=0,null=True, blank=True)
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    productStatus = models.TextField(max_length=10)
    def __str__(self):
        return f"{self.productImage} {self.productName} {self.ProductSku} {self.ProductNumber} {self.productPrice} {self.productCategory} {self.productStatus}"
class Customers(models.Model):
    customerName = models.CharField(max_length=100)
    customerEmail = models.CharField(max_length=50, unique=True)
    customerLocation = models.CharField(max_length=50)
    customerOrders = models.IntegerField(default=0, null=True, blank=True)
    cashSpent = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.customerName} {self.customerEmail} {self.customerLocation} {self.customerOrders} {self.cashSpent}"
class Orders(models.Model):
    OrderId = models.CharField(max_length=50)
    OrderNumber = models.IntegerField(default=0,null=True,blank=True)
    CustomerName = models.ForeignKey(Customers,on_delete=models.CASCADE)
    datePurchased = models.DateTimeField()
    paymentMethod = models.CharField(max_length=50)
    amountPaid = models.FloatField(default=0,null=True,blank=True)
    orderStatus = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.OrderId} {self.OrderNumber} {self.CustomerName} {self.datePurchased} {self.paymentMethod} {self.amountPaid} {self.orderStatus}"
class CustomUser(AbstractUser):

    fullname = models.CharField(max_length=140)
    email = models.EmailField(unique=True)
 
     
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]
    
# Create your models here.
