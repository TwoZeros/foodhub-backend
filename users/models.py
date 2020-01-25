from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fio= models.CharField(max_length = 500, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['fio','email','birth_date']
    

