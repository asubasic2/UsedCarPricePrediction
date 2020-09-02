from django.db import models


# Create your models here.
class Auto(models.Model):
    Proizvodjac = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Godiste = models.IntegerField(default=0)
    Kilometara = models.IntegerField(default=0)
    Gorivo = models.CharField(max_length=20)
    Kubika = models.FloatField(default=0)
    BrojVrata = models.CharField(max_length=5)
    Cijena = models.IntegerField(default=0)
    Kilovata = models.IntegerField(default=0)
    Tip = models.CharField(max_length=30)
    Pogon = models.CharField(max_length=20)
    Mjenjac = models.CharField(max_length=20)
    Emisija = models.CharField(max_length=10)
    Datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Proizvodjac


class Olx(models.Model):
    Proizvodjac = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Godiste = models.IntegerField(default=0)
    Kilometara = models.IntegerField(default=0)
    Gorivo = models.CharField(max_length=20)
    Kubika = models.FloatField(default=0)
    BrojVrata = models.CharField(max_length=5)
    Cijena = models.IntegerField(default=0)
    Kilovata = models.IntegerField(default=0)
    Tip = models.CharField(max_length=30)
    Pogon = models.CharField(max_length=20)
    Mjenjac = models.CharField(max_length=20)
    Emisija = models.CharField(max_length=10)
    Datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Proizvodjac




