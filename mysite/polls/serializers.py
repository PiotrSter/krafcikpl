from rest_framework import serializers
from .models import User, Supplier, Brewery, Type, Color, Capacity, Beer, Shop, Order

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['login', 'email', 'password', 'address', 'phone_number']

class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'surname', 'vechicle']

class BrewerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brewery
        fields = ['brewery_name']

class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ['type_of_beer']

class ColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Color
        fields = ['color']

class CapacitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Capacity
        fields = ['capacity']

class BeerSerializer(serializers.HyperlinkedModelSerializer):
    brewery = serializers.SlugRelatedField(queryset=Brewery.objects.all(), slug_field='brewery_name')
    type = serializers.SlugRelatedField(queryset=Type.objects.all(), slug_field='type_of_beer')
    color = serializers.SlugRelatedField(queryset=Color.objects.all(), slug_field='color')
    capacity = serializers.SlugRelatedField(queryset=Capacity.objects.all(), slug_field='capacity')
    #brewery = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='brewery-detail')
    #type = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='type-detail')
    #color = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='color-detail')
    #capacity = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='capacity-detail')

    class Meta:
        model = Beer
        fields = ['name', 'brewery', 'type', 'color', 'capacity']

class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'beer', 'price']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    supplier = serializers.SlugRelatedField(queryset=Supplier.objects.all(), slug_field='name')

    class Meta:
        model = Order
        fields = ['user', 'shop', 'supplier']