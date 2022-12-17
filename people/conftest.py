from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Permission
from people.models import Company, Visit
import pytest
from django.test import Client


@pytest.fixture
def user():
    u = User.objects.create(username='tadeusz')
    return u


@pytest.fixture
def users():
    lst = []
    for n in range(2):
        u = User.objects.create(username='tadeusz')
        lst.appendu(u)
    return lst


@pytest.fixture
def users_po_company():
    lst = []
    for n in range(2):
        u = User.objects.create(company=n)
        lst.appendu(u)
    return lst


@pytest.fixture  # tu przygotowujemy materiały do testów
def companies():
    lst = []
    for n in range(10):
        c = Company.objects.create(name_company=n, industry=n)
        lst.append(c)
    return lst


@pytest.fixture
def user_is_specialist():
    u = User.objects.filter(groups__name='Specialist').all
    return u


# @pytest.fixture
# def client():
#     client = Client() #W fiksturze client, wywoływanej przed każdym testem, tworzymy obiekt klienta.
#     return client


@pytest.fixture  # tu przygotowujemy materiały do testów
def companies():
    lst = []
    for n in range(10):
        c = Company.objects.create(name_company=n, industry=n)
        lst.append(c)
    return lst


# @pytest.fixture # tu przygotowujemy materiały do testów
# def persons():
#     lst = []
#     for n in range(10):
#         p = Person.objects.create(first_name=n, last_name=n)
#         lst.append(p)
#     return lst
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def user_user_compa(companies):
    company = companies[0]  ##jak to było z ta listą?
    userowy = User.objects.create(username='tadeusz', password='test', groups='test')
    user_companowy = User.objects.create(company=company)
    return (userowy + user_companowy)


@pytest.fixture
def user(companies):
    company = companies[0]  ##jak to było z ta listą?
    return User.objects.create(username='tadeusz', password='test', groups='test', company=company)


@pytest.fixture
def users(companies):
    lst = []
    for company in companies:
        userowy = User.objects.create(username='tadeusz', password='test', groups='test')
        user_companowy = User.objects.create(company=company)
        # m = User.objects.create(username='tadeuszowy', password='testpassw', groups='worker', company=company)
        lst.append(userowy)
        lst.append(user_companowy)
    return lst

#
# @pytest.fixture
# def users(companies):
#     lst = []
#     for company in companies:
#         m = User.objects.create(username='tadeuszowy', password='testpassw', groups='worker', company=company)
#         lst.append(m)
#     return lst


@pytest.fixture
def visit(users):
    user = users[0]  ##jak to było z ta listą?
    return Visit.objects.create(what_time='2022-12-28 12:00', location='Warszawski test', specialist=user, patient=user)


@pytest.fixture
def visites(users):
    lst = []
    for user in users:
        m = Visit.objects.create(what_time='2022-12-28 12:00', location='Warszawski test', specialist=user,
                                 patient=user)
        lst.append(m)
    return lst
