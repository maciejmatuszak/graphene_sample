from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.TextField(blank=True)
    email = models.EmailField()
