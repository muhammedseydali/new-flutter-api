from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, viewsets
from rest_framework.exceptions import APIException
from rest_framework.decorators import permission_classes
from .models import Cars, Cart, Order
from .serializers import CarSerializer, CartSerializer, OrderSerializer
# Create your views here.


class CarsView(ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer


class OrdersView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CartView(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer    