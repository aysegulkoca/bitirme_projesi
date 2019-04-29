from django.contrib import admin
from .models import Product, Version, Vulnerability

admin.site.register(Product)
admin.site.register(Version)
admin.site.register(Vulnerability)
# Register your models here.
