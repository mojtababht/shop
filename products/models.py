from django.db import models
from django.contrib.auth.models import User

class Category (models.Model):
    parent=models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE)
    title =models.CharField(max_length=50)
    description=models.TextField(blank=True)
    avatar=models.ImageField(blank=True,upload_to='categories/')
    is_enable=models.BooleanField(default=True)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    avatar=models.ImageField(blank=True,upload_to='products/')
    is_enable=models.BooleanField(default=True)
    categories=models.ManyToManyField('Category',blank=True)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    price=models.FloatField(default=50.0)
    is_top=models.BooleanField(default=False)

    def __str__(self):
        return self.title
    #


class File (models.Model):
    product=models.ForeignKey('product',on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    file=models.FileField(upload_to='files/%Y/%m/%d/')
    is_enable=models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)


class CartItem(models.Model):
    cart=models.ForeignKey('Cart',on_delete=models.CASCADE)
    product=models.ForeignKey('Product',on_delete=models.CASCADE)


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField(max_length=100)

class OrderItem(models.Model):
    product=models.ForeignKey('Product',on_delete=models.CASCADE)
    order=models.ForeignKey('Order',on_delete=models.CASCADE)