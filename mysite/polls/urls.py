from django.urls import path, include
from django.conf.urls import url
from .views import UserList, UserDetail, SupplierList, SupplierDetail, BreweryList, BreweryDetail, TypeList, \
    TypeDetail, ColorList, ColorDetail, CapacityList, CapacityDetail, BeerList, BeerDetail, ShopList, ShopDetail, \
    OrderList, OrderDetail

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    path('', UserList.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
    path('', SupplierList.as_view()),
    path('<int:pk>/', SupplierDetail.as_view())
]