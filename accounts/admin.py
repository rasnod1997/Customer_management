from django.contrib import admin
from .models import *
# * means we import all of our models such as Customer, Order , Product

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Tag)


# Register your models here.
