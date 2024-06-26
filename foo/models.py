from django.db import models

# Create your models here.
from django.db import models

class Restaurant(models.Model):
    zipcode = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    introduction = models.CharField(max_length=500)

