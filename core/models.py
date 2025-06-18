from django.db import models

# Create your models here.
class usuarios(models.Model):
    nome = models.CharField(max_length=100)