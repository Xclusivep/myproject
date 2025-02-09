from django.contrib import admin
# from django.db import admin
from .models import customer,product,Categories,Blog

admin.site.register(customer)
admin.site.register(product)
admin.site.register(Categories)
admin.site.register(Blog)
# Register your models here.
