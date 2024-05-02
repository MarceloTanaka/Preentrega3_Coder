from django.shortcuts import render

from . import models

def home(request):
    query = models.Cliente.objects.all()
    context = {"clientes": query}
    return render(request, "Clase/index.html", context)