from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy

def home(request):
    query = models.Cliente.objects.all()
    context = {"clientes": query}
    return render(request, "Cliente/index.html", context)

def cliente_create(request):
    if request.method == "POST":
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Cliente:home")
    else:
        form = forms.ClienteForm()
    return render(request, "Cliente/cliente_create.html", context={"form": form})

class ClienteDelete(DeleteView):
    model = models.Cliente
    template_name = "Cliente/cliente_delete.html"
    success_url = reverse_lazy("Cliente:home")

class ClienteDetail(DetailView):
    model = models.Cliente
    context_object_name = "cliente"

class ClienteUpdate(UpdateView):
    model = models.Cliente
    template_name = "Cliente/cliente_update.html"
    form_class = forms.ClienteForm
    success_url = reverse_lazy("Cliente:home")
