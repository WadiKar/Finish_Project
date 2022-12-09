from django.contrib import admin

# Register your models here.
from people.models import Company, Visit
# User


admin.site.register(Visit)
#admin.site.register(User)
admin.site.register(Company)
