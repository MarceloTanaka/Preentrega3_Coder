from django.shortcuts import render, redirect
from . import models, forms

def home(request):
    query = models.Producto.objects.all()
    context = {"productos": query}
    return render(request, "Producto/index.html", context)


def agregarproducto(request):
    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Producto:home")
    else:
        form = forms.ProductoForm()
    return render(request, "Producto/agregarproducto.html", context={"form": form})


