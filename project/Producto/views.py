from django.shortcuts import render, redirect
from . import models, forms
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

def home(request):
    query = models.Producto.objects.all()
    context = {"productos": query}
    return render(request, "Producto/index.html", context)

class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("Producto:home")
    template_name = "Producto/producto_create.html"

class ProductoDetail(DetailView):
    model = models.Producto
    context_object_name = "producto"

class ProductoUpdate(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("Producto:home")
    template_name = "Producto/producto_update.html"

class ProductoDelete(DeleteView):
    model = models.Producto
    template_name = "Producto/producto_delete.html"
    success_url = reverse_lazy("Producto:home")
