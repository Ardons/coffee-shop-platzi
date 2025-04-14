from django.contrib import admin
from .models import Product

class ProducAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'price']
    search_fields = ['name']
    
admin.site.register(Product, ProducAdmin)
