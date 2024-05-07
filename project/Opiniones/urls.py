from django.urls import path
from . import views

app_name = "Opiniones"

urlpatterns = [
    path("", views.home, name="home"),
    path("agregaropinion/", views.agregaropinion, name="agregaropinion")
]