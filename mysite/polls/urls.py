from django.urls import path, include
from django.conf.urls import url
from .views import UserList, UserDetail

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    path('', UserList.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
]