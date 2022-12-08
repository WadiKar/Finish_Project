from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth, Group
from django.contrib.auth import authenticate, login, logout

from media.forms import ReleaseAddForm
from media.models import Category, Release
from people.forms import  UserCreateForm, LoginForm
#from people.forms import ProfileAddForm,

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
        logout(request)  #
        return redirect('index')


class AddReleaseView(PermissionRequiredMixin, View):
    permission_required = ['media.add_release']

    def post(self, request, Category_pk):
        form = ReleaseAddForm(request.POST)
        category = Category.objects.get(pk=Category_pk)
        if form.is_valid():
            release = form.save(commit=False)
            release.category = category
            release.author_specialist = request.user  #
            release.save()
            return redirect('detail_release', Category_pk)


class ReleaseDetailView(View):

    def get(self, request,
            pk):  ## co to jest to pk, to id, ale jak!? jak to się dizieje ze czasem jest np movie.id i coś działa? albo to z user
        release = Release.objects.get(pk=pk)
        form = ReleaseAddForm()
        return render(request, 'movie_detail.html', {'movie': movie, 'form': form})