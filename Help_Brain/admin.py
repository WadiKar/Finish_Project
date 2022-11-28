from django.contrib import admin

# Register your models here.
from Portal.Help_Brain.models import Specialist, Company, Patient

admin.site.register(Specialist)
admin.site.register(Company)
admin.site.register(Patient)
# Specialist, Company, Patient