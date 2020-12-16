from .models import User, Supplier, Brewery, Type, Color, Capacity, Beer, Shop, Order
from .serializers import UserSerializer, SupplierSerializer, BrewerySerializer, TypeSerializer, \
    ColorSerializer, CapacitySerializer, BeerSerializer, ShopSerializer, OrderSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class UserList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

class SupplierList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    name = 'supplier-list'

class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    name = 'supplier-detail'

class BreweryList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer
    name = 'brewery-list'

class BreweryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer
    name = 'brewery-detail'

class TypeList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    name = 'type-list'

class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    name = 'type-detail'

class ColorList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    name = 'color-list'

class ColorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    name = 'color-detail'

class CapacityList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Capacity.objects.all()
    serializer_class = ColorSerializer
    name = 'capacity-list'

class CapacityDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Capacity.objects.all()
    serializer_class = CapacitySerializer
    name = 'capacity-detail'

class BeerList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
    name = 'beer-list'

class BeerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
    name = 'beer-detail'

class ShopList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    name = 'shop-list'

class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    name = 'shop-detail'

class OrderList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    name = 'order-list'

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    name = 'order-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'user': reverse(UserList.name, request=request),
                         'supplier': reverse(SupplierList.name, request=request),
                         'brewery': reverse(BreweryList.name, request=request),
                         'type': reverse(TypeList.name, request=request),
                         'color': reverse(ColorList.name, request=request),
                         'capacity': reverse(CapacityList.name, request=request),
                         'beer': reverse(BeerList.name, request=request),
                         'shop': reverse(ShopList.name, request=request),
                         'order': reverse(OrderList.name, request=request)
                         })