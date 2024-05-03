from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()
    pais = forms.InlineForeignKeyField