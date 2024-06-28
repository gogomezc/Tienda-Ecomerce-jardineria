from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Producto, Venta, DetalleVenta, Cliente
from .forms import ClienteCreateForm, ProductoForm

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

# CRUD Section
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

# Carrito Section
@login_required
def agregar_al_carrito(request, producto_id):
    cliente = request.user.cliente
    producto = get_object_or_404(Producto, id=producto_id)
    venta, created = Venta.objects.get_or_create(cliente=cliente, completo=False)

    detalle_venta, created = DetalleVenta.objects.get_or_create(
        venta=venta,
        producto=producto,
    )

    detalle_venta.cantidad += 1
    detalle_venta.save()

    return redirect('carrito')

@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(DetalleVenta, id=item_id)
    item.delete()
    return redirect('carrito')

@login_required
def incrementar_cantidad(request, item_id):
    item = get_object_or_404(DetalleVenta, id=item_id)
    item.cantidad += 1
    item.save()
    return redirect('carrito')

@login_required
def decrementar_cantidad(request, item_id):
    item = get_object_or_404(DetalleVenta, id=item_id)
    if item.cantidad > 1:
        item.cantidad -= 1
        item.save()
    return redirect('carrito')

@login_required
def carrito(request):
    cliente = request.user.cliente
    venta, created = Venta.objects.get_or_create(cliente=cliente, completo=False)
    items = venta.detalleventa_set.all()
    items_total = []
    total = 0

    for item in items:
        item_total = item.producto.precio * item.cantidad
        total += item_total
        items_total.append({
            'id': item.id,
            'producto': item.producto,
            'cantidad': item.cantidad,
            'total': item_total,
        })
    
    context = {
        'items': items_total,
        'total': total,
    }
    return render(request, 'store/carrito.html', context)