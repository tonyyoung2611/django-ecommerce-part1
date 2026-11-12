from django.contrib import admin
from .models import Store, Product, Profile, Order, OrderItem, Review

admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
