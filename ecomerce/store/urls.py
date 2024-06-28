# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.productos, name='productos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('carrito/', views.carrito, name='carrito'),
    path('rosas/', views.rosas, name='rosas'),
    path('crud/', views.crud, name='crud'),
    path('crear/<str:modelo>/', views.crear, name='crear'),
    path('modificar/<str:modelo>/<int:pk>/', views.modificar, name='modificar'),
    path('eliminar/<str:modelo>/<int:pk>/', views.eliminar, name='eliminar'),
]


