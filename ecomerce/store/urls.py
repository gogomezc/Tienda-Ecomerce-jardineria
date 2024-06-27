from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.productos, name='productos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('carrito/', views.carrito, name='carrito'),
    path('rosas/', views.rosas, name='rosas'),

]