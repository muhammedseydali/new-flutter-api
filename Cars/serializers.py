from django.rest_framework import serializers
from Api.models import account
from .models import Cars, Cart, Order
from Api.serializers import UserRegisterSerializer
from Api.models import account

class CarSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer(read_only=True)

    class Meta:
        model = Cars
        fields = ['user','car_model','car_year','car_color','car_price','car_image','car_description','car_status','car_created_at','car_created_by','car_is_deleted']

    def get_user(self, obj):
        return obj.user.full_name