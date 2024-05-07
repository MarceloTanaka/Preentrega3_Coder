from django.shortcuts import render, redirect
from . import models, forms

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
