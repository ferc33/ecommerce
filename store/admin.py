from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    # Configuración para la visualización de los campos en la lista de productos en el panel de administración
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')

    # Configuración para prellenar automáticamente el campo 'slug' con el valor del campo 'product_name'
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)    