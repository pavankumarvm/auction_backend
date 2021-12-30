from django.shortcuts import render
from rest_framework import generics, serializers

from .models import Category, Product
from .serializer import CategorySerializer, ProductSerializer

# Create your views here.


class CategoryList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset

    serializer_class = CategorySerializer


class ProductList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset

    serializer_class = ProductSerializer
