from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns =[
    path('categories/',create_category, name='create_category'),
    path('categorydetail/<int:id>/', categoryDetail, name='update_category'),
    path('products/',create_product, name='create_product'),
    path('productdetail/<int:id>/', productDetail, name='update_product'),
    path('createcustomer/',createCustomer ),
    path('updatecustomer/<int:id>/', updateCustomer),
    path('createorder/',createOrder),
    path('updateorder/<int:id>/',updateOrder),
    path('register/',registerUser),
    path('login/',loginUser),
    path('api/token/refresh',TokenRefreshView.as_view(),name="token_refresh"),
    path('exportorders/',exportorders),
    path('exportcustomers/',exportcustomers),
    path('getrecentorders/',getrecentorders)




]