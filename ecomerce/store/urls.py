from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.productos, name='productos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('carrito/', views.carrito, name='carrito'),
    path('rosas/', views.rosas, name='rosas'),
    path('crud/', views.crud, name='crud'),
    path('crear/', views.crear, name='crear'),
    path('crearcli/', views.crearcli, name='crearcli'),
    path('modificar/<int:cliente_id>/', views.modificar, name='modificar'),
]