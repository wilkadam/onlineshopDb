# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    name = models.CharField(null=True, max_length=15)
    last_name = models.CharField(null=True, max_length=20)
    phone = models.BigIntegerField()
    street = models.CharField(null=True, max_length=50)
    house_no = models.CharField(null=True, max_length=20)
    city = models.CharField(null=True, max_length=20)
    pin = models.IntegerField(null=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    brand = models.CharField(max_length=20, default="")
    price = models.IntegerField(default=0)
    product_img = models.ImageField(upload_to="images", default="product.jpg")
    product_img1 = models.ImageField(upload_to="images", default="product.jpg")
    product_img2 = models.ImageField(upload_to="images", default="product.jpg")
    stock = models.IntegerField(default=10)

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    qty = models.IntegerField()

    @property
    def price(self):
        return self.product.price

    @property
    def amount(self):
        return self.qty * self.product.price

    def __str__(self):
        return self.product.product_name + " by " + self.user.username


STATUS = (
    ('Złożone', 'Złożone'),
    ('Potwierdzone', 'Potwierdzone'),
    ('W przygotowaniu', 'W przygotowaniu'),
    ('Wsyłane', 'Wsyłane'),
    ('Dostarczone', 'Dostarczone'),
    ('Anulowane', 'Anulowane'),
)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone = models.BigIntegerField(null=True)
    house_no = models.CharField(null=True, max_length=20)
    street = models.CharField(null=True, max_length=50)
    city = models.CharField(null=True, max_length=20)
    total = models.FloatField()
    code = models.CharField(max_length=15, default="")
    placed_at = models.DateTimeField(auto_now_add=True)
    pin = models.IntegerField(null=True)


    def __str__(self):
        return self.code + " to " + self.first_name + "\t" + self.last_name

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS, default='Placed')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name + " by " + self.user.first_name

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_on = models.DateField(default=now, editable=False)

    def __str__(self):
        return self.user.first_name + " - " + self.product.product_name