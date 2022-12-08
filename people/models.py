import uuid

from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.id}"
        # # def __str__(self):
        #return self.user.username

class Patient(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    learned_profession = models.CharField(max_length=128)
    work_done = models.CharField(max_length=128)
    company_name = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, default = None)
    email = models.CharField(max_length=128)
    your_name = models.ForeignKey('Person', on_delete=models.CASCADE, null=True, default = None)

class Company(models.Model):
    name_company = models.CharField(max_length=256)
    industry = models.CharField(max_length=128)
    no_employee = models.IntegerField(blank=True, null =True)
    profile_com = models.ForeignKey('Person', on_delete=models.CASCADE, null=True, default = None)


class Specialist(models.Model):
    full_name = models.CharField(max_length=128)
    specialization = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    profile_spec = models.ForeignKey('Person', on_delete=models.CASCADE, null=True, default = None)
