from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model):
    Person_name = models.CharField(max_length=20)
    Person_email = models.CharField(max_length=50,null=True)
    Person_phno = models.CharField(max_length=10,null=True)
    user = models.ForeignKey(User ,on_delete=models.CASCADE,null=True)

def __str__(self):
    return self.name