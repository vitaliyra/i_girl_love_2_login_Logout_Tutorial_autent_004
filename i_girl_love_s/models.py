from django.db import models
from django.contrib.auth.models import User

class Sweetmeat(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): return self.name
   
