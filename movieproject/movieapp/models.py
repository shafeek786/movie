from django.db import models

# Create your models here.
from django.db.models import IntegerField


class Movie(models.Model):
    objects = None
    name= models.CharField(max_length=250)
    desc= models.TextField()
    year= IntegerField()
    img= models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
