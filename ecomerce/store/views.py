from django.shortcuts import render
from .models import Producto, Venta, DetalleVenta

def inicio(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'store/inicio.html', context)

def productos(request):
    context = {}
    return render(request, 'store/producto.html', context)

def nosotros(request):
    context = {}
    return render(request, 'store/nosotros.html', context)

def rosas(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'store/rosas.html', context)

def carrito(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        order, created = Venta.objects.get_or_create(cliente=cliente, completo=False)
        items = order.detalleventa_set.all()
        total = sum(item.producto.precio * item.cantidad for item in items)
    else:
        items = []
        total = 0
    context = {
        'items': items,
        'total': total,
    }
    return render(request, 'store/carrito.html', context)
