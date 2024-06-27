from django.shortcuts import render

def inicio(request):
    context = {}
    return render(request, 'store/inicio.html', context)

def productos(request):
    context = {}
    return render(request, 'store/producto.html', context)

def nosotros(request):
    context = {}
    return render(request, 'store/nosotros.html', context)

def rosas(request):
    context ={}
    return render(request, 'store/rosas.html', context)

def carrito(request):
    context = {}
    return render(request, 'store/carrito.html', context)