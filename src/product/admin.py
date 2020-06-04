from django.contrib import admin

# Register your models here.
# relative import because are in the same model
from .models import Product
admin.site.register(Product)
