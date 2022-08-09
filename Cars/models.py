from statistics import mode
from django.db import models

# Create your models here.

class Cars(models.Model):
    car_name = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_year = models.IntegerField()
    car_color = models.CharField(max_length=50)
    car_price = models.IntegerField()
    car_image = models.ImageField(upload_to='images/',null=True)
    car_description = models.TextField(max_length=100, null=True)
    car_status = models.BooleanField(default=True)
    car_created_at = models.DateTimeField(auto_now_add=True)
    car_created_by = models.ForeignKey('Api.account',on_delete=models.CASCADE, null=True)
    car_is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.car_name


class Cart(models.Model):
    car_id = models.ForeignKey(Cars, on_delete=models.CASCADE)
    car_color = models.CharField(max_length=50)
    cart_quantity = models.IntegerField()
    cart_created_by = models.OneToOneField('Api.account',on_delete=models.CASCADE)
    cart_is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.car_id.car_name


class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Completed', 'Completed'),
    )

    order_id = models.AutoField(primary_key=True)
    order_total = models.IntegerField()
    order_created_at = models.DateTimeField(auto_now_add=True)
    order_created_by = models.ForeignKey('Api.account',on_delete=models.CASCADE)
    order_is_deleted = models.BooleanField(default=False)
    order_status = models.CharField(max_length=9, choices=ORDER_STATUS_CHOICES,default='Active')

    def __str__(self):
        return self.order_id