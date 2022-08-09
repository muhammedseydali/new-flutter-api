from typing import ValuesView
from django.urls import path, include,re_path
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()

router.register('cars', views.Cars, basename='cars')
router.register('cart', views.Cart, basename='instructors')
router.register('order', views.Order, basename='instructors')



urlpatterns = [
    path('', include(router.urls)),
   
]

