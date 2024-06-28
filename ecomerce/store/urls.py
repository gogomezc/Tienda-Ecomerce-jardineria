from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.productos, name='productos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/', views.carrito, name='carrito'),
    path('rosas/', views.rosas, name='rosas'),
    path('crud/', views.crud, name='crud'),
    path('crear/<str:modelo>/', views.crear, name='crear'),
    path('modificar/<str:modelo>/<int:pk>/', views.modificar, name='modificar'),
    path('eliminar/<str:modelo>/<int:pk>/', views.eliminar, name='eliminar'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('incrementar/<int:item_id>/', views.incrementar_cantidad, name='incrementar_cantidad'),
    path('decrementar/<int:item_id>/', views.decrementar_cantidad, name='decrementar_cantidad')
]
