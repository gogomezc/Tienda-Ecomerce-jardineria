from django import forms
from .models import Producto, Cliente

class ClienteCreateForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['user', 'nombre', 'email']
        
  
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'digital', 'image']