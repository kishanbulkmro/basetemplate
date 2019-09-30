from django.db import models
from django.urls import reverse


class Shelf(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __str__(self):
        return self.name