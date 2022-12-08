from django import forms
from django.contrib.auth.models import User
from wtforms import ValidationError
import random as r

from people.models import Specialist,  Company, User, Person
# from people.models import Profile

# def random_number():
#     ph_no = []
#     ph_no.append(r.randint(6, 9))  # w zaleznosci kto kim jest
#
#     for i in range(1, 10):
#         ph_no.append(r.randint(0, 9))
#
#
# class ProfileAddForm(forms.Form):
#     user = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.RadioSelect)  # required=False nie bo bedziemy wybierac czy spec, czy firma
#     id_user = forms.IntegerField(validators=[random_number])
#     bio = forms.CharField(max_length=256)
#     location = forms.CharField(max_length=64)


class PatientAddForm(forms.Form):
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)
    learned_profession = forms.CharField(max_length=128)
    work_done = forms.CharField(max_length=128)
    patient = forms.ModelChoiceField(queryset=Company.objects.all(), required=False)
    email = forms.CharField(max_length=128)
    person_patient = forms.ModelChoiceField(queryset=Person.objects.all(), required=False)
    # profile = forms.ModelChoiceField(queryset=Profile.objects.all(), required=False)

class CompanyAddForm(forms.Form):
    name_company = forms.CharField(max_length=256)
    industry = forms.CharField(max_length=128)
    no_employee = forms.IntegerField()
    person_company = forms.ModelChoiceField(queryset=Person.objects.all(), required=False)
    # profile_com = forms.ModelChoiceField(queryset=Profile.objects.all(), required=False)

class SpecialistAddForm(forms.Form):
    full_name = forms.CharField(max_length=128)
    specialization = forms.CharField(max_length=128)
    description = forms.CharField(max_length=256)
    person_specialist = forms.ModelChoiceField(queryset=Person.objects.all(), required=False)
    # profile_spec = forms.ModelChoiceField(queryset=Profile.objects.all(), required=False)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, help_text=False)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(max_length=120, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=120, widget=forms.PasswordInput)
    #profile = forms.ModelChoiceField(queryset=Profile.objects.all(), widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            raise ValidationError('Hasła nie są takie same!!!')


