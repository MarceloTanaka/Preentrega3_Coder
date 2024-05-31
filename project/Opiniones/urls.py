from django.urls import path
from . import views

app_name = "Opiniones"

urlpatterns = [
    path("", views.home, name="home"),
    path("agregaropinion/", views.agregaropinion, name="agregaropinion"),
    path("opinion/opinion_delete/ <int:pk>", views.OpinionDelete.as_view(), name="opinion_delete"),
    path("opinion/opinion_update/ <int:pk>", views.OpinionUpdate.as_view(), name="opinion_update"),
]