from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Venta, DetalleVenta, Cliente 
from .forms import ClienteCreateForm
from django.urls import reverse_lazy
from .forms import ProductoForm 

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

 
# Starting CRUD section
def crud(request):
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    return render(request, 'store/crud.html', {'clientes': clientes, 'productos': productos})

def crear(request, modelo):
    if modelo == 'cliente':
        if request.method == 'POST':
            form = ClienteCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('crud')
        else:
            form = ClienteCreateForm()
    elif modelo == 'producto':
        if request.method == 'POST':
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('crud')
        else:
            form = ProductoForm()
    
    return render(request, 'store/crear.html', {'form': form, 'modelo': modelo})

def modificar(request, modelo, pk):
    if modelo == 'cliente':
        instance = get_object_or_404(Cliente, pk=pk)
        form_class = ClienteCreateForm
    elif modelo == 'producto':
        instance = get_object_or_404(Producto, pk=pk)
        form_class = ProductoForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('crud')
    else:
        form = form_class(instance=instance)
    
    return render(request, 'store/modificar.html', {'form': form, 'modelo': modelo})

def eliminar(request, modelo, pk):
    if modelo == 'cliente':
        instance = get_object_or_404(Cliente, pk=pk)
    elif modelo == 'producto':
        instance = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        instance.delete()
        return redirect('crud')
    
    return render(request, 'store/eliminar.html', {'instance': instance, 'modelo': modelo})
#termina crud section 

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
