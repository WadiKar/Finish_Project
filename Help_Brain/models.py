from django.db import models



class Patient(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    learned_profession = models.CharField(max_length=128)
    work_done = models.CharField(max_length=128)
    patient = models.ForeignKey('Company', on_delete=models.CASCADE)

Specialist, Company, Patient
class Company(models.Model):
    name_company = models.CharField(max_length=256)
    industry = models.CharField(max_length=128)
    nemployee = models.CharField(max_length=128)



class Specialist(models.Model):
    full_name = models.CharField(max_length=128)
    specialization = models.CharField(max_length=128)
    description= models.CharField(max_length=256)
