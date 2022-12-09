from django import forms
from django.contrib.auth.models import User
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
    #profile = forms.ModelChoiceField(queryset=Profile.objects.all(), widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = ['username']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            raise ValidationError('Hasła nie są takie same!!!')