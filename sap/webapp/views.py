from django.shortcuts import render

from sap.froms import ProductoSearchForm
from .models import Categoria, Producto, Cliente

def base(request):
    return render(request, 'base.html')

def index(request):
    categorias = Categoria.objects.all()
    return render(request, 'index.html', {'categorias': categorias})

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})


def buscar_producto(request):
    form = ProductoSearchForm(request.GET)
    productos = []

    if form.is_valid():
        productos = form.search()

    return render(request, 'buscar_producto.html', {'form': form, 'productos': productos})
