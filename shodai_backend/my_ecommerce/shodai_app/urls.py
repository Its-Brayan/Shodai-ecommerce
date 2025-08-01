from django.urls import path
from .views import *
urlpatterns =[
    path('categories/',create_category, name='create_category'),
    path('categorydetail/<int:id>/', categoryDetail, name='update_category'),
    path('products/',create_product, name='create_product'),
    path('productdetail/<int:id>/', productDetail, name='update_product'),
]