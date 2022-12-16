from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse

from media.forms import BookAddForm
from media.models import Author, Book


# Create your tests here.


def test_index_view():
    client = Client()  # otwieramy przegladarke
    url = reverse('index')  # mowimy na jaki url chcemy wejsc
    response = client.get(url)  # wchodzimy na url
    assert response.status_code == 200


@pytest.mark.django_db
class TestBooks:
    def test_books_view(self):
        client = Client()  # otwieramy przegladarke
        url = reverse('view_books')  # mowimy na jaki url chcemy wejsc
        response = client.get(url)  # wchodzimy na url
        assert response.status_code == 200


@pytest.mark.django_db
class TestAudiobooks:
    def test_audiobooks_view(self):
        client = Client()  # otwieramy przegladarke
        url = reverse('view_audiobooks')  # mowimy na jaki url chcemy wejsc
        response = client.get(url)  # wchodzimy na url
        assert response.status_code == 200


@pytest.mark.django_db
class TestReleases:
    def test_releases_view(self):
        client = Client()  # otwieramy przegladarke
        url = reverse('view_release')  # mowimy na jaki url chcemy wejsc
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
class TestAuthor:
    def test_author_view(self):
        client = Client()  # otwieramy przegladarke
        url = reverse('view_author')  # mowimy na jaki url chcemy wejsc
        response = client.get(url)  # wchodzimy na url
        assert response.status_code == 200


@pytest.mark.django_db
class TestAuthor:
    def test_create_author(self):
        client = Client()
        url = reverse('create_author')
        response = client.get(url)
        assert 200 == response.status_code


@pytest.mark.django_db
def test_create_author_post():
    data = {
        'fullname': 'testowy',
    }
    client = Client()
    url = reverse('create_author')
    response = client.post(url, data)
    assert response.status_code == 302
    assert Author.objects.get(fullname='testowy')


@pytest.mark.django_db
class TestAppointment:
    def test_appointment_author(self):
        client = Client()
        url = reverse('view_appointment')
        response = client.get(url)
        assert 200 == response.status_code


# BooksView(View):
@pytest.mark.django_db
def test_list_books_books(books):
    client = Client()
    url = reverse('view_books')
    response = client.get(url)
    book_context = response.context['books']
    assert book_context.count() == len(books)
    for b in books:
        assert b in book_context


# BooksView(View):
@pytest.mark.django_db
def test_list_books_categories(categories):
    client = Client()
    url = reverse('view_books')
    response = client.get(url)
    category_context = response.context['categories']
    assert category_context.count() == len(categories)
    for bc in categories:
        assert bc in category_context
# bookdetail
@pytest.mark.django_db
def test_list_book_detail(book):
    client = Client()
    url = reverse('detail_books', args=(book.id,)) #jakim cudem bez tego przcinka nie działa a z " , " i to w takim miejscu już dziala
    response = client.get(url)
    assert book == response.context['book']
    form = response.context['form']
    assert isinstance(form, BookAddForm)

# ------------------------------------------------------------------------------------------------------------------------------------------------





# BooksView(View): BookDetailView(View): AddBookView(UserPassesTestMixin, View): ReleasesView(View):ReleaseDetailView(View):
# RelsortView(View): AudiobooksView(View): AudiobookDetailView(View): AddAudiobookView(UserPassesTestMixin, View):
# CreateAuthorView(View): AuthorView(View): AuthorDetailView(View): AddPostView(UserPassesTestMixin, View):
# createbook



# def test_func(self):
#     division = Division.objects.get(short_name=self.kwargs['division'])
#     return self.request.user == division.director

# createbookpost
# @pytest.mark.django_db
# def test_create_book_post():
#     data = {
#         'title': 'testowaburza',
#         'year': 1999,
#         'relimg': 'test.png',
#     }
#
#     client = Client()
#     url = reverse('create_book')
#     response = client.post(url, data)
#     assert response.status_code == 302
#     assert Book.objects.get(title='testowaburza', year=1999, relimg='test.png')
#     # relimg, categories, authors, year, title


# class Release(models.Model):
#     title = models.TextField(max_length=200)
#     text = models.TextField(max_length=2000)
#     category_release = models.ForeignKey(Category, on_delete=models.CASCADE)
#     author_specialist = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     relimg = models.ImageField(upload_to='profile_images', default='test.png')
#     date = models.DateTimeField(auto_now_add=True)


@pytest.mark.django_db
def test_list_releases_authors(authors):
    client = Client()
    url = reverse('view_release')
    response = client.get(url)
    release_context = response.context['release']
    assert release_context.count() == len(authors)
    for m in authors:
        assert m in release_context

