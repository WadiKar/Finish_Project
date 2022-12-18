from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse


from django.utils.decorators import method_decorator

from media.conftest import user
from people.forms import CompanyForm, VisitAddForm
from people.models import User
from people.views import MyView


def test_index_view():
    client = Client()  # otwieramy przegladarke
    url = reverse('index')  # mowimy na jaki url chcemy wejsc
    response = client.get(url)  # wchodzimy na url
    assert response.status_code == 200


@pytest.mark.django_db
class TestSpecialist:
    def test_specialist_view(self):
        client = Client()  # otwieramy przegladarke
        url = reverse('view_specialist')  # mowimy na jaki url chcemy wejsc
        response = client.get(url)  # wchodzimy na url
        assert response.status_code == 200

@pytest.mark.django_db
class TestVisit:
    def test_visit_view(self):
        client = Client()  # otwieramy przegladarke
        url = reverse('make_appointment')  # mowimy na jaki url chcemy wejsc
        response = client.get(url)  # wchodzimy na url
        assert response.status_code == 200

#-------------------------------------------------------------------------------------------Nie dzialaja
# user = User.objects.create(username='testuser')
# user.set_password('12345')
# user.save()
#
# c = Client()
# logged_in = c.login(username='testuser', password='12345')
@pytest.mark.django_db

class VisitForCompany(TestCase):
    @pytest.mark.usefixtures("user_user_for_company")
    def test_CompanySeeVisit(self):
        c = Client()
        c.force_login(User.objects.get_or_create(username='test')[0])
        url = reverse('view_company')
        response =c.get(url)
        assert 200 == response.status_code
        self.assertContains(response, 'company0')



@pytest.mark.django_db
def test_visit_user_detail(visit):
    client = Client()
    url = reverse('detail_appointment', args=(visit.id,))
    response = client.get(url)
    assert visit == response.context['visit']
    form = response.context['form']
    assert isinstance(form, VisitAddForm)
# -------------------------------






# from django.views.generic.edit import UpdateView
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import UserPassesTestMixin
# from django.contrib.auth import authenticate, login
#
# @pytest.mark.django_db
# class TestUserOwnerMyView(UserPassesTestMixin):
#     def test_func(self):
#         self.object = self.get_object()
#         return self.request.user == self.object.user.is_specialist()
#
#
# class MyView(UpdateView, TestUserOwnerMyView()):
#     model = User
#
#     @method_decorator (login)
#     def dispatch(self, *args, **kwargs):
#         return super(MyView, self).dispatch(*args, **kwargs)



# class EditPost(UpdateView, TestUserOwnerOfPost):
#     model = User
#
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(EditPost, self).dispatch(*args, **kwargs)
