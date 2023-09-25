from django.shortcuts import render
from store.models import Product
# Create your views here.
def home(request):
    # Obtener todos los productos disponibles
    products = Product.objects.all().filter(is_available=True)

    # Crear el contexto con los productos obtenidos
    context = {
        'products': products,
    }

    # Renderizar la plantilla 'home.html' con el contexto
    return render(request, 'home.html', context)
