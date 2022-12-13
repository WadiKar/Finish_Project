from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth, Group, AbstractUser
from django.contrib.auth import authenticate, login, logout

import people
from media.models import Category, Release
from people.forms import UserCreateForm, LoginForm


class RegisterView(View):

    def get(self, request):
        form = UserCreateForm()

        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = UserCreateForm(request.POST)

        if form.is_valid():
            u = form.save(commit=False)
            u.set_password(form.cleaned_data['password'])
            u.save()
            return redirect("index")
        return render(request, 'form.html', {'form': form})


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        message = ""  # czemu wiadomosc jst pusta? skad to mewsage sie wzieło? Wiiałąm w innym projekcie ze to było importowane, to jest jakas funkcja czy w tym przypadku po prostu zmienna
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  #
                return redirect("index")
            message = "Nie poprawne hasło lub/i nazwa użytkownika"
        return render(request, 'form.html', {'form': form, 'message': message})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')

def is_member(user):
    return user.groups.filter(name='Member').exists()


class MyView(LoginRequiredMixin, UserPassesTestMixin, View):

    login_url = '/specialists/'
    redirect_field_name = 'create_audiobook'

    def test_func(self):
        return is_member(self.request.user)

        specialist = request.user.groups.all(name='Specialist')
        return render(request, 'listy2specialist.html', {'specialist': specialist})

class SpecialistView(View):
    def get(self, request):
        specialist = people.models.User.objects.all()
        return render(request, 'listy2specialist.html', {'specialist': specialist})

class SpecialistDetailView(View):

    def get(self, request, pk):
        specialist = people.models.User.objects.get(pk=pk)
        return render(request, 'detailspecialist.html', {'specialist': specialist})

# class SpecialistDetailView(View):
#
#     def get(self, request, pk):
#         autorzy = Author.objects.get(pk=pk)
#         return render(request, 'detailauthor.html', {'author': autorzy})

