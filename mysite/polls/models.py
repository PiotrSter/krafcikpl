from django.db import models

class User(models.Model):
    login = models.CharField(max_length=16)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=32)
    address = models.CharField(max_length=45)
    phone_number = models.IntegerField(max_length=9)

class Supplier(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    vechicle = models.CharField(max_length=45)

class Brewery(models.Model):
    brewery_name = models.CharField(max_length=45)


class Type(models.Model):
    type_of_beer = models.CharField(max_length=45)


class Color(models.Model):
    color = models.CharField(max_length=45)


class Capacity(models.Model):
    capacity = models.IntegerField(max_length=5)

class Beer(models.Model):
    name = models.CharField(max_length=45)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    capacity = models.ForeignKey(Capacity, on_delete=models.CASCADE)

class Shop(models.Model):
    name = models.CharField(max_length=45)
    beer = models.ManyToManyField(Beer)
    price = models.FloatField(max_length=5)

class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)




