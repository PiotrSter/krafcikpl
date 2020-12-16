from django.urls import path, include
from django.conf.urls import url
from .views import UserList, UserDetail, SupplierList, SupplierDetail, BreweryList, BreweryDetail, TypeList, \
    TypeDetail, ColorList, ColorDetail, CapacityList, CapacityDetail, BeerList, BeerDetail, ShopList, ShopDetail, \
    OrderList, OrderDetail, ApiRoot

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    path('user', UserList.as_view(), name=UserList.name),
    path('user/<int:pk>', UserDetail.as_view(), name=UserDetail.name),
    path('supplier', SupplierList.as_view(), name=SupplierList.name),
    path('supplier/<int:pk>', SupplierDetail.as_view(), name=SupplierDetail.name),
    path('brewery', BreweryList.as_view(), name=BreweryList.name),
    path('brewery/<int:pk>', BreweryDetail.as_view(), name=BreweryDetail.name),
    path('type', TypeList.as_view(), name=TypeList.name),
    path('type/<int:pk>', TypeDetail.as_view(), name=TypeDetail.name),
    path('color', ColorList.as_view(), name=ColorList.name),
    path('color/<int:pk>', ColorDetail.as_view(), name=ColorDetail.name),
    path('capacity', CapacityList.as_view(), name=CapacityList.name),
    path('capacity/<int:pk>', CapacityDetail.as_view(), name=CapacityDetail.name),
    path('beer', BeerList.as_view(), name=BeerList.name),
    path('beer/<int:pk>', BeerDetail.as_view(), name=BeerDetail.name),
    path('shop', ShopList.as_view(), name=ShopList.name),
    path('shop/<int:pk>', ShopDetail.as_view(), name=ShopDetail.name),
    path('order', OrderList.as_view(), name=OrderList.name),
    path('order/<int:pk>', OrderDetail.as_view(), name=OrderDetail.name),
    path('', ApiRoot.as_view(), name=ApiRoot.name)
]