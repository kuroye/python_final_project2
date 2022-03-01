from django.db import models

# Create your models here.

class Image(models.Model):

    image = models.ImageField(null=True, blank=True)
    path = models.CharField(max_length=255)
    result = models.CharField(max_length=50)

    class Meta:
        db_table = 'image'
