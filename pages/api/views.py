
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from django.shortcuts import render, redirect, reverse, get_object_or_404
# from django.http import HttpResponse
from pages.models import Product
from pages.api.serializers import ProductSerializer  


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return Response({'message': 'Product saved successfully', 'product': product.data}, status=200)
        return Response(product.errors, status=400) #####
    elif request.method == 'GET':
        products = Product.get_all_products()
        serializer = ProductSerializer(products, many = True)
        return Response({'message': 'Products data via GET METHOD have been received', 'prodcucts': serializer.data}, status=201)

@api_view(['GET','PUT', 'DELETE'])
def special(request, id):
    product = Product.objects.filter(id=id).first()

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response({'message': 'Special Product data via GET METHOD has been received', 'prodcuct': serializer.data}, status=201)

    elif request.method == 'PUT':
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Special Product data via PUT METHOD has been received', 'prodcuct': serializer.data}, status=200)
        return Response(serializer.errors, status=400)
  
    elif request.method == 'DELETE':
        product.delete()
        return Response({'message': 'Product Deleted Successfully'}, status= 204)