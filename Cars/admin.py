from django.contrib import admin

# Register your models here.
from .models import Cars, Cart, Order

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'car_model', 'car_year', 'car_color', 'car_price', 'car_image', 'car_description', 'car_status', 'car_created_at', 'car_created_by', 'car_is_deleted')
    list_filter = ('car_name', 'car_model', 'car_year', 'car_color', 'car_price', 'car_image', 'car_description', 'car_status', 'car_created_at', 'car_created_by', 'car_is_deleted')
    search_fields = ('car_name', 'car_model', 'car_year', 'car_color', 'car_price', 'car_image', 'car_description', 'car_status', 'car_created_at', 'car_created_by', 'car_is_deleted')
    list_per_page = 25

admin.site.register(Cars, CarAdmin)