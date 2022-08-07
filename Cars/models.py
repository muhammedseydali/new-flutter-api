from statistics import mode
from django.db import models

# Create your models here.

class Cars(models.Model):
    car_name = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_year = models.IntegerField(max_length=10)
    car_color = models.CharField(max_length=50)
    car_price = models.IntegerField(max_length=10)
    car_image = models.ImageField(upload_to='images/',null=True)
    car_description = models.TextField()
    car_status = models.BooleanField(default=True)
    car_created_at = models.DateTimeField(auto_now_add=True)
    car_created_by = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    car_is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.car_name


class Cart(models.Model):
    car_id = models.ForeignKey('Cars',on_delete=models.CASCADE)
    car_color = models.CharField(max_length=50)
    cart_quantity = models.IntegerField(max_length=10)
    cart_created_by = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    cart_is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.car_id.car_name


class Order(models.Model):
    ORDER_STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Completed', 'Completed'),
    )

    order_id = models.AutoField(primary_key=True)
    order_total = models.IntegerField(max_length=10)
    order_created_at = models.DateTimeField(auto_now_add=True)
    order_created_by = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    order_is_deleted = models.BooleanField(default=False)
    order_status = models.CharField(max_length=8, choices=ORDER_STATUS_CHOICES,default='Active')

    def __str__(self):
        return self.order_id