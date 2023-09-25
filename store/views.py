from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
def store(request, category_slug=None):
    # Obtener la categoría correspondiente al 'category_slug' (opcional)
    categories = None
    products = None

    if category_slug != None:
        # Si se proporciona un 'category_slug', obtener la categoría correspondiente
        # utilizando la función 'get_object_or_404' y filtrar los productos en base a esa categoría
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        products_count = products.count()
    else:
        # Si no se proporciona un 'category_slug', obtener todos los productos disponibles
        # filtrando aquellos con 'is_available=True'
        products = Product.objects.all().filter(is_available=True)
        products_count = products.count()

    # Crear un diccionario de contexto con los productos y la cantidad de productos
    context = {
        'products': products,
        'product_count': products_count,
    }

    # Renderizar la plantilla 'store/store.html' con el contexto
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    return render(request, 'store/product_detail.html')