from statistics import mode
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User

# Create your models here.

class Usuario(User):
    nome = models.CharField(max_length= 180)

    def str(self):
        return self.nome