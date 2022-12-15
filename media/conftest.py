# import pytest
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User, Permission
#
# from media.models import Author, Book, Audiobook, Category, Release
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
# @pytest.fixture
# def author():
#     lst = []
#     for n in range(10):
#         p = Author.objects.create(fullname=n)
#         lst.append(p)
#     return lst
#
#
#
#
#
#
#
#
# #####
#
