from statistics import mode
from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_lenght=180)

    def __str__(self):
        return self.nome