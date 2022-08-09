from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, viewsets
from rest_framework.exceptions import APIException
from rest_framework.decorators import permission_classes
from .models import Cars, Cart, Order
from .serializers import CarsSerializer, CartSerializer, OrderSerializer
# Create your views here.


class Cars(ModelViewSet):
    queryset = Cars.objects.filter(is_deleted=False).order_by('-date_added')
    serializer_class = CarsSerializer
    

