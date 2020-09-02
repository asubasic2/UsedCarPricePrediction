from datetime import timedelta

from background_task.models import Task
from django.urls import path
from . import views
from .tasks import scrapeaj

urlpatterns = [
    path("automobili", views.DajProcijenjenaAuta, name="dajAuta"),
    path("procijeni", views.ProcijeniAuto, name="ProcijeniAuto"),
    path("procijeniMin", views.procijeniMin, name="ProcijeniSaMinimalnimParametrima"),
    path("Proizvodjaci", views.DajProizvodjace, name="Proizvodjaci")
]

scrapeaj(repeat=Task.DAILY, repeat_until=None)
