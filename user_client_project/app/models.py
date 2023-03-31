
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Client(models.Model):
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)

    def __str__(self): 
        return self.client_name

class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def __str__(self): 
        return self.name

    