import datetime

from django.db import models
from django.utils import timezone


class Tulokset(models.Model):
    ottelupari = models.CharField(max_length=100)
    tulos = models.CharField(max_length=5, blank=True)
    pelattu = models.BooleanField()

    def __str__(self):
        return self.ottelupari


class Osallistujat(models.Model):
    osallistuja = models.CharField(max_length=30, unique=True)
    pisteet = models.IntegerField(default=0)

    def __str__(self):
        return self.osallistuja


class Veikkaukset(models.Model):
    osallistujat = models.ForeignKey(Osallistujat, on_delete=models.CASCADE)
    tulokset = models.ForeignKey(Tulokset, on_delete=models.CASCADE)
    veikkaus = models.CharField(max_length=5)

    def __str__(self):
        return self.veikkaus
