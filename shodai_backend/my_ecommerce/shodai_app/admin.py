from django.contrib import admin
from .models import *
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customers)
admin.site.register(Orders)
admin.site.register(CustomUser)

# Register your models here.
