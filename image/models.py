from django.db import models

# Create your models here.

class Image(models.Model):

    path = models.CharField(max_length=255)
    result = models.CharField(max_length=50)

