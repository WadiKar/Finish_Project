import pytest

from django.test import Client
from django.urls import reverse

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Permission

from media.models import Author, Book, Audiobook, Category, Release
from people.models import Company, Visit, User


# book(m2m author, categories)
# audiobook(m2mauthor, categories)
# release(fkcategory_release, author_specialist)


#
# --------------------------------------------------------------------------------------------------------BOOKS
# relimg, year, title, categories, authors,
@pytest.fixture
def books():
    lst = []
    category = Category.objects.create(name='testowany')
    author = Author.objects.create(fullname='testowy')
    for n in range(10):
        p = Book.objects.create(title=n, year=2020)
        p.categories.add(category)
        p.authors.add(author)
        lst.append(p)
    return lst

@pytest.fixture
def books_category():
    lst = []
    category = Category.objects.create(name='testowany')
    catego_2 = Category.objects.create(name='testowany2')
    author = Author.objects.create(fullname='testowy')
    for n in range(10):
        p = Book.objects.create(title=n, year=2020)
        p.categories.add(category)
        p.authors.add(author)
        lst.append(p)
    for n in range(10):
        p = Book.objects.create(title=n, year=2020)
        p.categories.add(catego_2)
        p.authors.add(author)
        lst.append(p)
    return lst


@pytest.fixture
def book(books):
    book = books[0]  ##jak to było z ta listą?

    return Book.objects.create(title='Owoc który sie nie kula', year='2022', relimg='test.png')


# time, authors, categories, book
@pytest.fixture
def audiobooks(books):
    lst = []
    category = Category.objects.create(name='testowany')
    author = Author.objects.create(fullname='testowy')
    for book in books:
        p = Audiobook.objects.create(time=book, book=book)
        p.categories.add(category)
        p.authors.add(author)
        lst.append(p)
    return lst


@pytest.fixture
def audiobo():
    lst = []
    category = Category.objects.create(name='testowany')
    author = Author.objects.create(fullname='testowy')
    for a in range(10):
        p = Audiobook.objects.create(time=23, book=a)
        p.categories.add(category)
        p.authors.add(author)
        lst.append(p)
    return lst


@pytest.fixture
def audiobook(books):
    book = books[0]  ##jak to było z ta listą?
    return Book.objects.create(time=23, book=book)


# --------------------------------------------------------------------------------------------------------AUTHOR
@pytest.fixture
def authors():
    lst = []
    for n in range(0):
        p = Author.objects.create(fullname=n)
        lst.append(p)
    return lst


@pytest.fixture
def author(books):
    book = books[0]  ##jak to było z ta listą?
    return Book.objects.create(title='Owoc który sie nie kula', year=2022)


# --------------------------------------------------------------------------------------------------------CATEGORIES
@pytest.fixture
def categories():
    lst = []
    for n in range(10):
        p = Category.objects.create(name=n)
        lst.append(p)
    return lst


# ---------------------------------------------------------------------------------------------------------RELEASES        POJEDYNCZE I MNOGIE
@pytest.fixture
def release_categories(categories):
    lst = []
    for category in categories:
        m = Release.objects.create(title="mis", text="witamins", category_release=category, relimg='biznesxxi.png')
        lst.append(m)
    return lst


@pytest.fixture
def releas_categories(categories):
    category = categories[0]  ##jak to było z ta listą?
    return Release.objects.create(title='Owoc ktory się nie kula', date='2020', relimg='test.png',
                                  text='Nie kula się owoc pracy', category_release=category)


@pytest.fixture
def releases_authors(authors):
    lst = []
    for author in authors:
        m = Release.objects.create(title="mis", text="witamins", category_release=author, relimg='test.png')
        lst.append(m)
    return lst


@pytest.fixture
def releas_authors(authors):
    author = authors[0]  ##jak to było z ta listą?
    return Release.objects.create(title='Najzdrowsze owoce', date='2022', relimg='test.png',
                                  text='Wbrew pozorom malo jest witamin w cytrusach', author_specialist=author)


# -------------------------------------------------------------------------------------------------------------USER

@pytest.fixture
def user():
    u = User.objects.create(username='tadeusz')
    return u


# ---------------------------------------------------------------------------------------------------- USER
@pytest.fixture
def user_with_permission():
    u = User.objects.create(username='tadeusz')
    permission = Permission.objects.get(codename='add_comment')
    u.user_permissions.add(permission)
    return u


# UserPassesTestMixin,
# PermissionRequiredMixin
@pytest.fixture
def user_with_permission():
    if User.is_specialist():
        u = User.objects.create(username='tadeusz')
        u.add(User)
    return u

# Bookpojedynczy
# @pytest.fixture
# def book(categories, authors):
#     category = categories[0]
#     author = authors[0]  ##jak to było z ta listą?
#     b = Book.objects.create(
#         title='Po burzy zawsze przychodzi słońce',
#         year='2022',
#         relimg='test.png',
#     )
#     b.categories.add(categories)
#     b.author.add(authors)
#     return b


# relimg, categories, authors, year, title
# # Bookslista
# @pytest.fixture
# def bookscategory(categories):
#     lst = []
#     # category = Category.objects.create(name='testcategory')
#     for category in categories:
#         b = Book.objects.create(
#             title="mis",
#             year='1999',
#             relimg='test.png'
#         )
#         b.categories.add(category)
#         lst.append(b)
#     return lst
