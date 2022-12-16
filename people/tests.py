from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse


# def test_details(client):
#     response = client.get('sith/list/')  # Pobieramy stronę metodą GET.
#     assert response.status_code == 200  # Czy odpowiedź HTTP to 200 OK.
#     # Czy widok zwrócił w kontekście DOKŁADNIE 2 Sithów?
#     assert len(response.context['sith']) == 2
from people.forms import CompanyForm


def test_index_view():
    client = Client()  # otwieramy przegladarke
    url = reverse('index')  # mowimy na jaki url chcemy wejsc
    response = client.get(url)  # wchodzimy na url
    assert response.status_code == 200


@pytest.mark.django_db  #
def test_list_person(persons):
    client = Client()
    url = reverse('list_person')
    response = client.get(url)
    persons_context = response.context['persons']
    assert persons_context.count() == len(persons)  # count
    for p in persons:  #
        assert p in persons_context


@pytest.mark.django_db
class TestCompany:
    def test_VisitForCompany(self):
        client = Client()
        url = reverse('view_company')
        what_time = {
            'name': 'Bambus',
        }
        response = client.post(url, what_time)
        assert 200 == response.status_code
