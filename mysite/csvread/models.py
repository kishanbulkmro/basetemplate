from django.db import models

# Create your models here.

class UploadFileForm(models.Model):

    CompanyName = models.CharField(max_length=500)
    CountryName = models.CharField(max_length=500)
    StandNumber = models.CharField(max_length=500)
    Address = models.CharField(max_length=500)
    Website = models.CharField(max_length=500)
    ProductCatogery = models.CharField(max_length=500)
    Year = models.CharField(max_length=500)
    Email = models.CharField(max_length=500)
    Phone = models.CharField(max_length=500)

    def __str__(self):
        return self.CompanyName


