from django.contrib import admin

# Register your models here.
from .models import Cars, Cart, Order

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'car_model', 'car_year', 'car_color', 'car_price', 'car_image', 'car_description', 'car_status', 'car_created_at', 'car_created_by', 'car_is_deleted')
    list_filter = ('car_name', 'car_model', 'car_year', 'car_color', 'car_price', 'car_image', 'car_description', 'car_status', 'car_created_at', 'car_created_by', 'car_is_deleted')
    search_fields = ('car_name', 'car_model', 'car_year', 'car_color', 'car_price', 'car_image', 'car_description', 'car_status', 'car_created_at', 'car_created_by', 'car_is_deleted')
    list_per_page = 25

admin.site.register(Cars, CarAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ('car_id', 'car_color', 'cart_quantity', 'cart_created_by', 'cart_is_deleted')
    list_filter = ('car_id', 'car_color', 'cart_quantity', 'cart_created_by', 'cart_is_deleted')

    search_fields = ('car_id', 'car_color', 'cart_quantity', 'cart_created_by', 'cart_is_deleted')
admin.site.register(Cart, CartAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_total', 'order_created_at', 'order_created_by', 'order_is_deleted', 'order_status')
    list_filter = ('order_total', 'order_created_at', 'order_created_by', 'order_is_deleted', 'order_status')
    search_fields = ('order_total', 'order_created_at', 'order_created_by', 'order_is_deleted', 'order_status')
admin.site.register(Order, OrderAdmin)