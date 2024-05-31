from django import forms
from . import models

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = ["nombre", "descripcion", "precio", "imagen"]