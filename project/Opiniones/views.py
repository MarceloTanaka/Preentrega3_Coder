from django.shortcuts import render, redirect
from . import models, forms
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy

def home(request):
    query = models.Opinion.objects.all()
    context = {"opiniones": query}
    return render(request, "Opiniones/index.html", context)

def agregaropinion(request):
    if request.method == "POST":
        form = forms.OpinionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Opiniones:home")
    else:
        form = forms.OpinionForm()
    return render(request, "Opiniones/agregaropinion.html", context={"form": form})

class OpinionDelete(DeleteView):
    model = models.Opinion
    template_name = "Opiniones/opinion_delete.html"
    success_url = reverse_lazy("Opinion:home")

class OpinionUpdate(UpdateView):
    model = models.Opinion
    template_name = "Opiniones/opinion_update.html"
    form_class = forms.OpinionForm
    success_url = reverse_lazy("Opiniones:home")

