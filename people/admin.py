from django.contrib import admin

# Register your models here.
from people.models import Company, Visit, User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


admin.site.register(Visit)
admin.site.register(Company)
admin.site.register(User, UserAdmin)