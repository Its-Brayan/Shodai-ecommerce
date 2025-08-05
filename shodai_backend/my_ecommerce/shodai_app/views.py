from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.core.paginator import Paginator
from .serializers import *

@api_view(['GET', 'POST'])
def create_category(request):
 
    if request.method =='POST':
        serializer = CategorySerializer(data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        page = int(request.GET.get('page',1))
        page_size =int(request.GET.get('itemsPerPage',5))
        search_query = request.GET.get('search', '')
        categories = Category.objects.all()
        if search_query:
            categories = categories.filter(categoryName__icontains=search_query)
        paginator = Paginator(categories, page_size)  
        page_obj = paginator.get_page(page) 
        serializer = CategorySerializer(page_obj.object_list, many=True)
        return Response({'count':paginator.count,
                         'page':page,
                         'results':serializer.data},status=status.HTTP_200_OK)
    
@api_view(['GET','PUT', 'DELETE'])    
def categoryDetail(request, id):
   
    category = Category.objects.get(id=id)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def create_product(request):
   
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        page = int(request.GET.get('page'))
        page_size = int(request.GET.get('itemsPerPage',5))
        search_query = request.GET.get('search','')
        specific_product=request.GET.get('sproduct','')
        productcategory = request.GET.get('category','')
        productstatus = request.GET.get('status','')
        filterbyprice = request.GET.get('price_range','')
        products = Product.objects.all()
        if filterbyprice:
            try:
                parts = filterbyprice.split('-')
                min_price = float(parts[0]) if parts[0] else 0
                max_price = float(parts[1]) if len(parts) > 1 and parts[1] else None
                if min_price:
                    products = products.filter(productPrice__gte=min_price)
                if max_price is not None:
                    products = products.filter(productPrice__lte=max_price)
            except (ValueError, IndexError):
             return Response({"error": "Invalid price range format"}, status=400)
        if productstatus:
            products = products.filter(productStatus__iexact=productstatus)
        if productcategory:
            products = products.filter(productCategory__categoryName__exact=productcategory)
        if specific_product:
            products = products.filter(productName__iexact=specific_product)
        if search_query:
            products = products.filter(productName__icontains=search_query)
        
        paginator = Paginator(products,page_size)
        page_obj = paginator.get_page(page)
        serializer = ProductSerializer(page_obj.object_list, many=True)
        return Response({'count':paginator.count,
                         'page':page,
                         'results':serializer.data}, status=status.HTTP_200_OK)
@api_view(['PUT', 'DELETE'])
def productDetail(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['POST','GET'])
def createCustomer(request):
    if request.method=="POST":
        data = request.data
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        page = request.GET.get('page')
        page_size = request.GET.get('itemsPerPage',5)
        search_query = request.GET.get('search','')
        customer_location = request.GET.get('location','')
        customer = Customers.objects.all()
        if customer_location:
            customer = customer.filter(customerLocation__iexact=customer_location)
        if search_query:
            customer = customer.filter(customerEmail__icontains=search_query)
        paginator = Paginator(customer, page_size)
        page_obj = paginator.get_page(page)
        serializer = CustomerSerializer(page_obj.object_list, many=True)
        return Response({
            'count':paginator.count,
            'page':page,
            'results':serializer.data}, status=status.HTTP_200_OK)
@api_view(['GET','PUT','DELETE'])
def updateCustomer(request, id):
    customer = Customers.objects.get(id=id)
    if request.method=='GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method =="PUT":
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['POST','GET'])
def createOrder(request):
    if request.method=="POST":
       serializer = OrdersSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method=="GET":
        page=request.GET.get('page')
        page_size = request.GET.get('itemsPerPage')
        search_query=request.GET.get('search')
        orderstatus = request.GET.get('status','')
        orders = Orders.objects.all()
        if orderstatus:
            orders=orders.filter(orderStatus__iexact=orderstatus)
       
        if search_query:
            orders = orders.filter(OrderId__icontains =search_query)
        paginator = Paginator(orders,page_size)
        page_obj = paginator.get_page(page)

        serializer = OrdersSerializer(page_obj.object_list, many=True)
        return Response({
            'count':paginator.count,
            'page':page,
            'results':serializer.data,
            }, status=status.HTTP_200_OK)
@api_view(['GET','PUT','DELETE'])
def updateOrder(request,id):
    order = Orders.objects.get(id=id)
    if request.method=="GET":
        serializer= OrdersSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=="PUT":
        serializer=OrdersSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method=="DELETE":
         order.delete()
         return Response(status=status.HTTP_204_NO_CONTENT) 
# Create your views here.
