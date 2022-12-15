from datetime import datetime
from django_flatpickr.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from django import forms
from django.contrib.auth.models import User
from django.forms import SelectDateWidget, DateInput
from wtforms import ValidationError
import random as r

from people.models import Company, User, Visit


# from people.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, help_text=False)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(max_length=120, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=120, widget=forms.PasswordInput)

    # profile = forms.ModelChoiceField(queryset=Profile.objects.all(), widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            raise ValidationError('Hasła nie są takie same!!!')


class SpecialistForm(forms.Form):
    full_name = forms.CharField(max_length=60)
    psychotherapy_technique = forms.CharField(max_length=120)
    bio = forms.CharField(max_length=450)

class CompanyForm(forms.Form):
    class Meta:
        model = Company
        fields = "__all__"


class DateTimePicker:
    pass


class VisitAddForm(forms.ModelForm):
    # what_time = forms.DateField(label='Date', required=True, widget=DateTimePicker(), input_formats=["%Y-%m-%d"])
    # location = forms.CharField(max_length=128)
    # specialist = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.RadioSelect)
    # patient = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.RadioSelect)

    class Meta:
        model = Visit
        fields = ['what_time', 'location', 'specialist', 'patient']
        # force-use a specific kind of widget for a field
        widgets = {
            'what_time':  DateTimePickerInput()
        }

        def clean(self):
            cleaned_data = super().clean()
            res_date = cleaned_data.get('date')

            # booking for past date
            today = datetime.date.today()
            if res_date < today:
                raise ValidationError('Booking in the past is not allowed')

            # the room is already booked on that day
            already_reserved = list(self.instance.visit.filter(date=res_date))
            if len(already_reserved) > 0:
                raise ValidationError(f'The room is already booked on {res_date}')
