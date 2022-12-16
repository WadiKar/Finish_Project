from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Permission
from people.models import Company, Visit
import pytest
from django.test import Client
#
#
# @pytest.fixture
# def user():
#     u = User.objects.create(username='tadeusz')
#     return u
#
# @pytest.fixture
# def user():
#     u = UserAdmin.objects.create(username='Zdzisław')
#     return u



# @pytest.fixture
# def client():
#     client = Client() #W fiksturze client, wywoływanej przed każdym testem, tworzymy obiekt klienta.
#     return client


@pytest.fixture # tu przygotowujemy materiały do testów
def companies():
    lst = []
    for n in range(10):
        c = Company.objects.create(name_company=n, industry=n)
        lst.append(c)
    return lst