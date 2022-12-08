from django.contrib import admin

# Register your models here.
from people.models import Specialist, Patient, Company, Person

# from people.models import Profile

admin.site.register(Person)
# admin.site.register(Profile)
admin.site.register(Specialist)
admin.site.register(Patient)
admin.site.register(Company)
