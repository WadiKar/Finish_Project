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
    """
    Tworzony jest formularz ułatwiający tworzenie nowego użytkownika, Tu jest działanie rejestreacji.
    Tu jest używane żądanie do zmiany stanu systemu dlatego korzystanmy z GET i POST. GET należy używać tylko w przypadku żądań, które nie mają wpływu na stan systemu.
     a POST wprowadza zmiany w bazie danych, dlatego używany jest cleaned_data który weryfiukuje wpowadzone dane. GET  łączy przesłane dane w łańcuch i używa go do utworzenia adresu URL.
    """

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
    """
    Wykorzystywany formularz logowania
Sprawdza czy uzytkownik jest ten za ktorego sie podaje. czy taki user i takie haslo wystepuje w zapisanej bazie danych. 2if - jesli nie ma dostepnego takiego hasalai user w bazie
podaje infrmacje o błędzie. i prowadzi na index czyli stronę główną dla niezalogowanych.
    """

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
    """ Widok do wylogowywaynia użytkownika. Pobierany jest obiekt HttpRequest i nie zwraca żadnej wartości.Zwracany jest uzytkownika na stronę główną zdefiniowana poprzez index"""

    def get(self, request):
        logout(request)
        return redirect('index')


def is_member(user):
    return user.groups.filter(name='Specialist').exists()


class MyView(LoginRequiredMixin, UserPassesTestMixin, View):
    """
    Tworzony jest widok dodawania spotkania. Uzywana jest funkcja
    :is_member: aby wyselekcjonować użytkowników specjalisci z ktorymi mozna się umawiac

    """
    login_url = '/specialists/'
    redirect_field_name = 'create_audiobook'  # myview

    def test_func(self):
        return is_member(self.request.user)

        specialist = request.user.groups.all(name='Specialist')
        return render(request, 'listy2specialist.html', {'specialist': specialist})


class SpecialistView(View):
    """
    Widok przedstawiający listę uzytkowników z grupy Specjaliści
    """

    def get(self, request):
        specialist = people.models.User.objects.filter(groups__name='Specialist').all
        return render(request, 'listy2specialist.html', {'specialist': specialist})


class SpecialistDetailView(View):
    """
    Szczegóły danego specjalisty. Jego dane, metody działania i wykształcenie
    """

    def get(self, request, pk):
        specialist = people.models.User.objects.get(pk=pk)
        return render(request, 'detailspecialist.html', {'specialist': specialist})


class Make_appointment(View):
    """
    Tworzenie spotkanie wykorzystujac formularz. w metodzie POST sprawdzane jest czy wporowadzane dane przy tworzeniu są pooprawne i zapisuje.
    """

    def get(self, request):
        form = VisitAddForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = VisitAddForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'form.html', {'form': form})


class VisitView(View):
    """
    Generuje listę wszystkich wizyt.
    """

    def get(self, request):
        visit = Visit.objects.all()
        return render(request, 'list2visit.html', {'visits': visit})


class Detail_appointment(View):
    """
    Wyswietlane są szczegóły wizyt, tzn mojesce, czas, kto i jaki specjalista. uzywa formularza. Szczegóły wyświetlają się po podaniu id wizyty.
    """
    def get(self, request, pk):
        visita = Visit.objects.get(pk=pk)
        form = VisitAddForm()
        return render(request, 'detailappointment.html', {'visit': visita, 'form': form})



class VisitForCompanyView(View):
    """
    Widok tylko dla pracodawny. Liczacy sumy odbytych spotkach
    :suma: podaje i liczy ilość odbytych spotkan
    """
    def get(self, request):
        employees = request.user.company.Employees.all()
        suma = 0
        for employee in employees.iterator():
            suma += employee.Patient.count()
        return render(request, 'listy2company.html', {'suma': suma})  # {'company': company}
