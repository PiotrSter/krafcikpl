from .models import User, Supplier, Brewery, Type, Color, Capacity, Beer, Shop, Order
from .serializers import UserSerializer, SupplierSerializer, BrewerySerializer, TypeSerializer, \
    ColorSerializer, CapacitySerializer, BeerSerializer, ShopSerializer, OrderSerializer
from rest_framework import generics

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class BreweryList(generics.ListCreateAPIView):
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer

class BreweryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer

class TypeList(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class ColorList(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class ColorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class CapacityList(generics.ListCreateAPIView):
    queryset = Capacity.objects.all()
    serializer_class = ColorSerializer

class CapacityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Capacity.objects.all()
    serializer_class = CapacitySerializer

class BeerList(generics.ListCreateAPIView):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer

class BeerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer

class ShopList(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer