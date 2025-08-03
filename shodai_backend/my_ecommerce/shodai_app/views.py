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
        products = Product.objects.all()
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
# Create your views here.
