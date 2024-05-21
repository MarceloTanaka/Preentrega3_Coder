from django.shortcuts import render
from .forms import CustomAuthentificationForm
from django.contrib.auth.views import LoginView

def home(request):
    return render(request, "core/index.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthentificationForm
    template_name = "core/login.html"