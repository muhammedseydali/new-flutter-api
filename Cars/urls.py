from typing import ValuesView
from django.urls import path, include,re_path
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()

router.register('cars', views.CarsView, basename='cars')
router.register('cart', views.CartView, basename='instructors')
router.register('order', views.OrdersView, basename='instructors')



urlpatterns = [
    path('', include(router.urls)),
   
]

