import pytest

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Permission

from media.models import Author, Book, Audiobook, Category, Release
from people.models import Company, Visit, User


#
#
# @pytest.fixture
# def books():
#     lst = []
#     for n in range(10):
#         p = Book.objects.create(title=n, year=n, authors=n, categories=n)
#         lst.append(p)
#     return lst
#
#


@pytest.fixture
def authors():
    lst = []
    for n in range(2):
        p = Author.objects.create(fullname=n)
        lst.append(p)
    return lst(n)

@pytest.fixture
def categories():
    lst = []
    for n in range(10):
        p = Category.objects.create(name=n)
        lst.append(p)
    return lst


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
#
# UserPassesTestMixin,
# PermissionRequiredMixin
@pytest.fixture
def user_with_permission():
    if User.is_specialist():
        u = User.objects.create(username='tadeusz')
        u.add(User)
    return u


@pytest.fixture
def release_categories(categories):
    lst = []
    for category in categories:
        m = Release.objects.create(title="mis", text="witamins", category_release=category, relimg='biznesxxi.png')
        lst.append(m)
    return lst


@pytest.fixture
def releases_authors(authors):
    lst = []
    for author in authors:
        m = Release.objects.create(title="mis", text="witamins", category_release=author, relimg='test.png')
        lst.append(m)
    return lst



@pytest.fixture
def user():
    u = User.objects.create(username='tadeusz')
    return u