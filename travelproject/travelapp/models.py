from django.db import models

# Create your models here.
class Place(models.Model):
    heading = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()