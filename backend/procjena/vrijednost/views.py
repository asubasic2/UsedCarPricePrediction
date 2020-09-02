import os

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AutoSerializer, AutoSerializerMin
from django.http import JsonResponse
from .models import Auto
from .Prediktor import Prediktor
import pandas as pd
import json
from background_task import background

p = Prediktor(r'C:\Users\Admir\Django\procjena\vrijednost\Automobili.csv')
df = pd.read_csv(r'C:\Users\Admir\Django\procjena\vrijednost\Automobili.csv',
                 names=['Proizvodjac', 'Model', 'Godiste', 'Kilometara', 'Gorivo', 'Kubikaza',
                        'BrojVrata', 'Cijena', 'Kilovata', 'Tip', 'Pogon', 'Mjenjac', 'Emisija'], encoding='utf-8')


# Create your views here.

@api_view(["GET"])
def DajProcijenjenaAuta(request):
    auta = Auto.objects.all()

    serializer = AutoSerializer(auta, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def DajProizvodjace(request):
    Proizvodjac = df.Proizvodjac.unique()
    Proizvodjac = sorted(Proizvodjac)
    lista = []
    for i in range(len(Proizvodjac)):
        tmp = df[df.Proizvodjac == Proizvodjac[i]]
        modeli = tmp.Model.unique()
        modeli = modeli.tolist()
        modeli = sorted(modeli)
        lista.append({"Proizvodjac": Proizvodjac[i], "Model": modeli})
    Auta = json.dumps(lista)
    return Response(Auta)


@api_view(["POST"])
def ProcijeniAuto(request):
    auto = [request.data['Proizvodjac'], request.data['Model'], request.data['Godiste'], request.data['Kilometara'],
            request.data['Kubika'], request.data['Kilovata'], request.data['Gorivo'], request.data['BrojVrata'],
            request.data['Tip'], request.data['Pogon'], request.data['Mjenjac'], request.data['Emisija']]
    print(auto)
    cijena = p.Predvidi(auto)
    request.data['Cijena'] = int(cijena)
    serializer = AutoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def procijeniMin(request):
    auto = [request.data['Proizvodjac'], request.data['Model'], request.data['Godiste']]
    cijena = p.PredvidiMin(auto)
    request.data['Cijena'] = int(cijena)
    serializer = AutoSerializerMin(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
