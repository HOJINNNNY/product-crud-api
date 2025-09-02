from django.contrib import admin
from .models import Tag, ProductOption, Product

admin.site.register(Tag)
admin.site.register(ProductOption)
admin.site.register(Product)