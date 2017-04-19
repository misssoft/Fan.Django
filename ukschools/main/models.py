from django.db import models

# Create your models here.

class School (models.Model):
    name = models.CharField(max_length = 250)
    phase = models.CharField(max_length = 50)
    type = models.CharField(max_length = 50)
    ofsted = models.CharField(max_length = 50)
    ofstedInspected = models.DateTimeField(auto_now=False)
    religious = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 20)
    address = models.CharField(max_length = 100)
    postcode = models.CharField(max_length = 10)