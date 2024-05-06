from django.shortcuts import render, redirect
from . import models

def home(request):
    query = models.Opinion.objects.all()
    context = {"opiniones": query}
    return render(request, "Opiniones/index.html", context)
