from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth, Group, AbstractUser
from django.contrib.auth import authenticate, login, logout

import people
from media.models import Category, Release
from people.forms import UserCreateForm, LoginForm, VisitAddForm
from people.models import Visit, Company


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

    def get(self, request, pl):
        specialist = people.models.User.objects.get(pk=pl)
        return render(request, 'detailspecialist.html', {'specialist': specialist})


# class Make_appointment(View):
#     form = VisitAddForm()


# class AddMovieView(View): #PermissionRequiredMixin,
#     # permission_required = ['media.add_visit']
#
#     def get(self, request):
#         form = VisitAddForm()
#         return render(request, 'form.html', {'form': form})
#
#     def post(self, request):
#         form = VisitAddForm()(request.POST)  #
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             year = form.cleaned_data['year']
#             director = form.cleaned_data['director']
#             Movie.objects.create(title=title, year=year,
#                                  director=director)  # po jednej stronie jest nazwa dla django a druga dla bazy dnych?
#             return redirect('/')
#         return render(request, 'form.html', {
#             'form': form})  # co własciwie, jaka funkce robia te {'form, albo movies, czy jest miedzy tym contextem róznica?)


class Make_appointment(View):

    def get(self, request):
        form = VisitAddForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = VisitAddForm(request.POST)
        if form.is_valid():  # valid sprawdza czy pola ktore są w formsach są zapisae? i pobiera je na podstawie form = StudioAddForm()?
            form.save()
        return render(request, 'form.html', {'form': form}, )




class Detail_appointment(View):
    def get(self, request, pk):
        visita = Visit.objects.get(pk=pk)
        return render(request, 'detailappointment.html', {'visit': visita})

class CompanyVisitView(View):
    def get(self, request):
        company = Company.objects.all()
        return render(request, 'listy2company.html', {'company': company})
