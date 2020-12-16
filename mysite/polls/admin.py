from django.contrib import admin
from .models import User, Supplier, Brewery, Type, Color, Capacity, Beer, Shop, Order

# Register your models here.

admin.site.register(User)
admin.site.register(Supplier)
admin.site.register(Brewery)
admin.site.register(Type)
admin.site.register(Color)
admin.site.register(Capacity)
admin.site.register(Beer)
admin.site.register(Shop)
admin.site.register(Order)
