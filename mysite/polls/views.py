from .models import Client, Supplier, Brewery, Type, Color, Capacity, Beer, Shop, Order
from .serializers import ClientSerializer, SupplierSerializer, BrewerySerializer, TypeSerializer, \
    ColorSerializer, CapacitySerializer, BeerSerializer, ShopSerializer, OrderSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions
from django_filters import AllValuesFilter, NumberFilter, FilterSet

class ClientList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-list'
    filter_fields = ['name', 'surname', 'address', 'phone_number']
    search_fields = ['name', 'surname', 'address', 'phone_number']
    ordering_fields = ['name', 'surname', 'address', 'phone_number']

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    name = 'client-detail'

class SupplierList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    name = 'supplier-list'
    filter_fields = ['name', 'surname']
    search_fields = ['name', 'surname']
    ordering_fields = ['name', 'surname']

class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    name = 'supplier-detail'

class BreweryList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer
    name = 'brewery-list'
    filter_fields = ['brewery_name']
    search_fields = ['brewery_name']
    ordering_fields = ['brewery_name']


class BreweryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer
    name = 'brewery-detail'

class TypeList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    name = 'type-list'
    filter_fields = ['type_of_beer']
    search_fields = ['type_of_beer']
    ordering_fields = ['type_of_beer']

class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    name = 'type-detail'

class ColorList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    name = 'color-list'
    filter_fields = ['color']
    search_fields = ['color']
    ordering_fields = ['color']

class ColorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    name = 'color-detail'

class CapacityList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Capacity.objects.all()
    serializer_class = CapacitySerializer
    name = 'capacity-list'
    filter_fields = ['capacity']
    search_fields = ['capacity']
    ordering_fields = ['capacity']


class CapacityDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Capacity.objects.all()
    serializer_class = CapacitySerializer
    name = 'capacity-detail'

class BeerList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
    name = 'beer-list'
    filter_fields = ['name', 'brewery', 'type', 'color', 'capacity']
    search_fields = ['name', 'brewery', 'type', 'color', 'capacity']
    ordering_fields = ['name', 'brewery', 'type', 'color', 'capacity']

class BeerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
    name = 'beer-detail'

class ShopFilter(FilterSet):
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')
    shop_name = AllValuesFilter(field_name='name')

    class Meta:
        moder = Shop
        fields = ['min_price', 'max_pirce', 'shop_name']

class ShopList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_class = ShopFilter
    name = 'shop-list'

class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    name = 'shop-detail'

class OrderList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    name = 'order-list'
    filter_fields = ['client']
    search_fields = ['client']
    ordering_fields = ['client']

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    name = 'order-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'client': reverse(ClientList.name, request=request),
                         'supplier': reverse(SupplierList.name, request=request),
                         'brewery': reverse(BreweryList.name, request=request),
                         'type': reverse(TypeList.name, request=request),
                         'color': reverse(ColorList.name, request=request),
                         'capacity': reverse(CapacityList.name, request=request),
                         'beer': reverse(BeerList.name, request=request),
                         'shop': reverse(ShopList.name, request=request),
                         'order': reverse(OrderList.name, request=request)
                         })