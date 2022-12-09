from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()


# Create your models here.


class Company(models.Model):
    name_company = models.CharField(max_length=256)
    industry = models.CharField(max_length=64)
    employees = models.ManyToManyField(User)


class Visit(models.Model):
    time =models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=128)
    specialist = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Company, on_delete=models.CASCADE)

# UserPassedTestMixin
