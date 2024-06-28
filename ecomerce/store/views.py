from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Venta, DetalleVenta, Cliente
from .forms import ClienteCreateForm


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

 
def crud(request):
    clientesListados = Cliente.objects.all()
    return render(request, 'store/crud.html',{"cliente":   clientesListados})

def crear(request, *args, **kwargs):
    form = ClienteCreateForm()
    context = {
        'form': form
    }
    return render(request, 'store/crear.html', context)

def crearcli(request):
    if request.method == 'POST':
        form = ClienteCreateForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data('user')
            nombre = form.cleaned_data('nombre')
            email = form.cleaned_data('email')
           
            c, created = Cliente.objects.get_or_create(user=user, nombre=nombre, email=email)
            c.save()
            return redirect('crud')
    else:
        form = ClienteCreateForm()
    return render(request, 'store/crear.html', {'form': form})


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
