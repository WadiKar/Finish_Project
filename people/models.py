


from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

# User = get_user_model()

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    company = models.ForeignKey('Company', related_name='Employees', null=True, on_delete=models.SET_NULL)

    def is_specialist(self):
        return self.groups.filter(name='Specialist').exists()
    def is_company(self):
        return self.groups.filter(name='Company').exists()


class Company(models.Model):
    name_company = models.CharField(max_length=256)
    industry = models.CharField(max_length=64)
    #employees = models.ManyToManyField(User)

    def __str__(self):
        return self.name_company


class Visit(models.Model):
    what_time = models.DateTimeField()
    location = models.CharField(max_length=128)
    specialist = models.ForeignKey(User, related_name='Specialist', null=True, on_delete=models.SET_NULL)
    patient = models.ForeignKey(User, related_name='Patient', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.location, self.what_time.strftime('%Y-%m-%d %H:%M')}"
# 2022-12-28 12:00:00