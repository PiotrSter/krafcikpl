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