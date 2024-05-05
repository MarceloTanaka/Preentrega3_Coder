from django.shortcuts import render
from . import models

def home(request):
    query = models.Producto.objects.all()
    context = {"producto": query}
    return render(request, "Producto/index.html", context)
