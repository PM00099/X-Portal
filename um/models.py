from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Xuser(models.Model):
    fname = models.CharField(max_length=50);
    lname = models.CharField(max_length=50);
    email = models.CharField(max_length=25);
    phone = models.CharField(max_length=13);
    age = models.IntegerField();
    user = models.OneToOneField(User,on_delete=models.CASCADE)