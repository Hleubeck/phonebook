from django.db import models
from django.utils import timezone


class Categories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, blank=True)
    createdata = models.DateTimeField(default=timezone.now)
    country = models.CharField(max_length=255, blank=True)
    countrycode = models.CharField(max_length=10, blank=True)
    state = models.CharField(max_length=100, blank=True)
    uf = models.CharField(max_length=5, blank=True)
    ddd = models.CharField(max_length=10, blank=True)
    tel = models.CharField(max_length=15)
    email = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    hidecontact = models.BooleanField(default=True)

    def __str__(self):
        return self.name
