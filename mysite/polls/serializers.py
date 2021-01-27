from rest_framework import serializers
from .models import Client, Supplier, Brewery, Type, Color, Capacity, Beer, Shop, Order

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'address', 'phone_number']

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

    class Meta:
        model = Beer
        fields = ['name', 'brewery', 'type', 'color', 'capacity']

#class ShopBeerSerializer(serializers.HyperlinkedModelSerializer):
    #class Meta:
        #model = Beer
        #fields = ['name']

class ShopSerializer(serializers.HyperlinkedModelSerializer):
    #beer = ShopBeerSerializer(many=True, read_only=False)
    #beer = serializers.HyperlinkedRelatedField(many=True, read_only=False, view_name='beer-detail')

    class Meta:
        model = Shop
        fields = ['name', 'beer', 'price']

#class OrderUserSerializer(serializers.HyperlinkedModelSerializer):
    #class Meta:
        #model = User
        #fileds = ['login']

#class OrderShopSerializer(serializers.HyperlinkedModelSerializer):
    #class Meta:
        #model = Shop
        #fields = ['name']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    #user = OrderUserSerializer(many=True, read_only=False)
    #shop = OrderShopSerializer(many=True, read_only=False)
    supplier = serializers.SlugRelatedField(queryset=Supplier.objects.all(), slug_field='name')

    class Meta:
        model = Order
        fields = ['client', 'shop', 'supplier']
