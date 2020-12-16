from rest_framework import serializers
from .models import User, Supplier, Brewery, Type, Color, Capacity, Beer, Shop, Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['login', 'email', 'password', 'address', 'phone_number']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'surname', 'vechicle']

class BrewerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Brewery
        fields = ['brewery_name']

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['type_of_beer']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color']

class CapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Capacity
        fields = ['capacity']

class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = ['name', 'brewery', 'type', 'color', 'capacity']

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'beer', 'price']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'shop', 'supplier']

# class UserSerializer(serializers.Serializer):
#     login = serializers.CharField(max_length=16)
#     email = serializers.CharField(max_length=255)
#     password = serializers.CharField(max_length=32)
#     address = serializers.CharField(max_length=45)
#     phone_number = serializers.IntegerField(max_length=9)
#
#     def create(self, validated_data):
#         return User.object.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.login = validated_data.get('login', instance.login)
#         instance.email = validated_data.get('email', instance.email)
#         instance.password = validated_data.get('password', instance.password)
#         instance.address = validated_data.get('address', instance.address)
#         instance.phone_number = validated_data.get('phone_number', instance.phone_number)
#         instance.save()
#         return instance
#
# class SupplierSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=45)
#     surname = serializers.CharField(max_length=45)
#     vechicle = serializers.CharField(max_length=45)
#
#     def create(self, validated_data):
#         return Supplier.object.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.surname = validated_data.get('surname', instance.surname)
#         instance.vechicle = validated_data.get('vechicle', instance.vechicle)
#         instance.save()
#         return instance
#
# class Brewery(serializers.Serializer):
#     brewery_name = serializers.CharField(max_length=45)
#
#     def create(self, validated_data):
#         return Brewery.object.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.brewery_name = validated_data.get('brewery_name', instance.brewery_name)
#         instance.save()
#         return instance
#
# class Type(serializers.Serializer):
#     type_of_beer = serializers.CharField(max_length=45)
#
#     def create(self, validated_data):
#         return Type.object.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.type_of_beer = validated_data.get('type_of_beer', instance.type_of_beer)
#         instance.save()
#         return instance
#
# class Color(serializers.Serializer):
#     color = serializers.CharField(max_length=45)
#
#     def create(self, validated_data):
#         return Color.object.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.color = validated_data.get('color', instance.color)
#         instance.save()
#         return instance
#
# class Capacity(serializers.Serializer):
#     capacity = serializers.IntegerField(max_length=5)
#
#     def create(self, validated_data):
#         return Capacity.object.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.capacity = validated_data.get('capacity', instance.capacity)
#         instance.save()
#         return instance
#
# class Beer(serializers.Serializer):
#     name = serializers.CharField(max_length=45)
#     brewery = serializers.ForeignKey(Brewery)
#     type = serializers.ForeignKey(Type)
#     color = serializers.ForeignKey(Color)
#     capacity = serializers.ForeignKey(Capacity)
#
#     def create(self, validated_data):
#         return Beer.object.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.brewery = validated_data.get('brewery', instance.brewery)
#         instance.type = validated_data.get('type', instance.type)
#         instance.color = validated_data.get('color', instance.color)
#         instance.capacity = validated_data.get('capacity', instance.capacity)
#         instance.save()
#         return instance
#
# class Shop(serializers.Serializer):
#     name = serializers.CharField(max_length=45)
#     beer = serializers.ManyToManyField(Beer)
#     price = serializers.FloatField(max_length=5)
#
#     def create(self, validated_data):
#         return Shop.object.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.beer = validated_data.get('beer', instance.beer)
#         instance.price = validated_data.get('price', instance.price)
#         instance.save()
#         return instance
#
# class Order(serializers.Serializer):
#     user = serializers.OneToOneField(User)
#     shop = serializers.OneToOneField(Shop)
#     supplier = serializers.ForeignKey(Supplier)
#
#     def create(self, validated_data):
#         return Order.object.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.user = validated_data.get('user', instance.user)
#         instance.shop = validated_data.get('beer', instance.shop)
#         instance.supplier = validated_data.get('supplier', instance.supplier)
#         instance.save()
#         return instance