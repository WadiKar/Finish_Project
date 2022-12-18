from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse

from media.forms import BookAddForm, AudiobookAddForm
from media.models import Author, Book

# Create your tests here.
from people.conftest import User


def test_index_view():
    client = Client()  # otwieramy przegladarke
    url = reverse('index')  # mowimy na jaki url chcemy wejsc
    response = client.get(url)  # wchodzimy na url
    assert response.status_code == 200


@pytest.mark.django_db
# class TestBooks:
def test_books_view():
    client = Client()  # otwieramy przegladarke
    url = reverse('view_books')  # mowimy na jaki url chcemy wejsc
    response = client.get(url)  # wchodzimy na url
    assert response.status_code == 200


@pytest.mark.django_db
def test_book_detail(book):
    client = Client()
    url = reverse('detail_books',
                  args=(book.id,))  # jakim cudem bez tego przcinka nie działa a z " , " i to w takim miejscu już dziala
    response = client.get(url)
    assert book == response.context['book']
    form = response.context['form']
    assert isinstance(form, BookAddForm)


@pytest.mark.django_db
def test_list_books_categories(categories):
    client = Client()
    url = reverse('view_books')
    response = client.get(url)
    category_context = response.context['categories']
    assert category_context.count() == len(categories)
    for bc in categories:
        assert bc in category_context


@pytest.mark.django_db
# class TestAudiobooks:
def test_audiobooks_view():
    client = Client()  # otwieramy przegladarke
    url = reverse('view_audiobooks')  # mowimy na jaki url chcemy wejsc
    response = client.get(url)  # wchodzimy na url
    assert response.status_code == 200

    # @pytest.mark.django_db
    # def test_audiobook_detail(audiobook):
    #     client = Client()
    #     url = reverse('detail_audiobook',  args=(audiobook.id,))  # jakim cudem bez tego przcinka nie działa a z " , " i to w takim miejscu już dziala
    #     response = client.get(url)
    #     assert audiobook == response.context['audiobooks']
    #     form = response.context['form']
    #     assert isinstance(form, AudiobookAddForm)
    #
    # @pytest.mark.django_db
    # def test_audiobook_detail(audiobo):
    #     client = Client()
    #     url = reverse('detail_audiobook',  args=(audiobo.id,))  # jakim cudem bez tego przcinka nie działa a z " , " i to w takim miejscu już dziala
    #     response = client.get(url)
    #     assert audiobo == response.context['audiobooks']
    #     form = response.context['form']
    #     assert isinstance(form, AudiobookAddForm)


@pytest.mark.django_db
# class TestReleases:
def test_releases_view():
    client = Client()  # otwieramy przegladarke
    url = reverse('view_release')  # mowimy na jaki url chcemy wejsc
    response = client.get(url)  # wchodzimy na url
    assert response.status_code == 200


@pytest.mark.django_db
def test_list_releases_categories(release_categories):
    client = Client()
    url = reverse('view_release')
    response = client.get(url)
    release_context = response.context['release']
    assert release_context.count() == len(release_categories)
    for m in release_categories:
        assert m in release_context


@pytest.mark.django_db
def test_specialist_view():
    client = Client()  # otwieramy przegladarke
    url = reverse('view_specialist')  # mowimy na jaki url chcemy wejsc
    response = client.get(url)  # wchodzimy na url
    assert response.status_code == 200


@pytest.mark.django_db
# class TestAuthor:
def test_author_view():
    client = Client()  # otwieramy przegladarke
    url = reverse('view_author')  # mowimy na jaki url chcemy wejsc
    response = client.get(url)  # wchodzimy na url
    assert response.status_code == 200


@pytest.mark.django_db
# class TestAuthor:
def test_create_author():
    client = Client()
    url = reverse('create_author')
    response = client.get(url)
    assert 200 == response.status_code


@pytest.mark.django_db
class VisitForCompany(TestCase):
    @pytest.mark.usefixtures("user_user_for_specialist")
    def test_create_author_post(self):
        data = {
            'fullname': 'tey autor'}
        client = Client()  # ------------------------------------superuser usergrups?
        client.force_login(User.objects.get_or_create(username='specialisttest')[0])
        url = reverse('create_author')
        response = client.post(url, data)
        assert response.status_code == 302
        self.assertRedirects(response, reverse("view_author"))
        response2 = client.get(reverse("view_author"))  # spr czy sie dodał
        self.assertContains(response2, 'tey autor')  # sprawdza czy jest zawartość na stronie
        assert response2.status_code == 200


# class AuthorView(View):

@pytest.mark.django_db
class TestAppointment:
    def test_appointment(self):
        client = Client()
        url = reverse('view_appointment')
        response = client.get(url)
        assert 200 == response.status_code


@pytest.mark.django_db
# class TestAppointment:
def test_appointment():
    client = Client()
    url = reverse('view_appointment')
    response = client.get(url)
    assert 200 == response.status_code


# ---------------------------------------------------------------------------------------------NIE DZIAŁAJĄ
# BooksView(View):
@pytest.mark.django_db
def test_list_books_books(books):
    client = Client()
    url = reverse('view_books')
    response = client.get(url, {'category': 1})
    book_context = response.context['books']
    assert book_context.count() == len(books)
    for b in books:
        assert b in book_context


@pytest.mark.django_db
def test_list_books_books(books_category):
    client = Client()
    url = reverse('view_books')
    response = client.get(url, {'category': ""})
    book_context = response.context['books']
    assert book_context.count() == len(books_category)
    for b in books_category:
        assert b in book_context


@pytest.mark.django_db
def test_list_books_filter(books_category):
    client = Client()
    url = reverse('view_books')
    response = client.get(url, {'category': 1})
    book_context = response.context['books']
    assert book_context.count() == 10
    for b in book_context:
        assert b in books_category

# !


# self.user = User.objects.create_user(username='testuser', password='12345')
# login = self.client.login(username='testuser', password='12345')

# ------------------------------------------------------------------------------------------------------------------------------------------------


# BooksView(View): BookDetailView(View): AddBookView(UserPassesTestMixin, View): ReleasesView(View):ReleaseDetailView(View):
# RelsortView(View): AudiobooksView(View): AudiobookDetailView(View): AddAudiobookView(UserPassesTestMixin, View):
# CreateAuthorView(View): AuthorView(View): AuthorDetailView(View): AddPostView(UserPassesTestMixin, View):
# createbook


# def test_func(self):
#     division = Division.objects.get(short_name=self.kwargs['division'])
#     return self.request.user == division.director
