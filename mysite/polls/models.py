from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=32)
    address = models.CharField(max_length=45)
    phone_number = models.IntegerField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name+' '+self.surname


class Supplier(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    vechicle = models.CharField(max_length=45)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name+' '+self.surname


class Brewery(models.Model):
    brewery_name = models.CharField(max_length=45)

    class Meta:
        ordering = ('brewery_name',)

    def __str__(self):
        return self.brewery_name


class Type(models.Model):
    type_of_beer = models.CharField(max_length=45)

    class Meta:
        ordering = ('type_of_beer',)

    def __str__(self):
        return self.type_of_beer


class Color(models.Model):
    color = models.CharField(max_length=45)

    class Meta:
        ordering = ('color',)

    def __str__(self):
        return self.color


class Capacity(models.Model):
    capacity = models.IntegerField()

    class Meta:
        ordering = ('capacity',)

    def __str__(self):
        return str(self.capacity)


class Beer(models.Model):
    name = models.CharField(max_length=45)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    capacity = models.ForeignKey(Capacity, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=45)
    beer = models.ManyToManyField(Beer)
    price = models.FloatField(max_length=5)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

