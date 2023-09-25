from django.contrib import admin
from .models import (Category)


class CategoryAdmin(admin.ModelAdmin):
    """La funcionalidad de prepopulated_fields es útil para generar
      valores automáticos en campos relacionados o derivados, lo que puede 
    ahorrar tiempo al usuario y garantizar la consistencia de los datos."""

    prepopulated_fields = {'slug' : ('category_name',)}
    list_display =  ('category_name','slug')

admin.site.register(Category, CategoryAdmin)

