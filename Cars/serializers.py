from rest_framework import serializers
from Api.models import account
from .models import Cars, Cart, Order
from Api.serializers import UserDataSerializer
from Api.models import account

class CarSerializer(serializers.ModelSerializer):
    user = UserDataSerializer(read_only=True)

    class Meta:
        model = Cars
        fields = ['user','car_name', 'car_model','car_year','car_color','car_price','car_image','car_description','car_status','car_created_at','car_created_by','car_is_deleted']

    def get_user(self, obj):
        return obj.user.full_name

class OrderSerializer(serializers.ModelSerializer):
    user = UserDataSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['user','order_total','order_created_at','order_created_by','order_is_deleted','order_status']

    def get_user(self, obj):
        return obj.user.user__name


class CartSerializer(serializers.ModelSerializer):
    user = UserDataSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ['user','car_id','car_color','cart_quantity','cart_created_by','cart_is_deleted']

    def get_user(self, obj):
        return obj.user.user__name        