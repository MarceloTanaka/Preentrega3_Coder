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

def producto_detail(request, pk):
    query = models.Producto.objects.get(id=pk)
    return render(request, "Producto/producto_detail.html", {"producto": query})

def producto_update(request, pk: int):
    query = models.Producto.objects.get(id=pk)
    if request.method == "POST":
        form = forms.ProductoForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("Producto:home")
    else:
        form = forms.ProductoForm(instance=query)
    return render(request, "Producto/producto_update.html", context={"form": form})

def producto_delete(request, pk: int):
    query = models.Producto.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("Producto:home")
    return render(request, "Producto/producto_delete.html", context={"producto": query})
