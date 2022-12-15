# from django.test import TestCase
# import pytest
# from django.test import Client
# from django.urls import reverse
# # Create your tests here.
#
#
# def test_index_view():
#     client = Client()  # otwieramy przegladarke
#     url = reverse('index')  # mowimy na jaki url chcemy wejsc
#     response = client.get(url)  # wchodzimy na url
#     assert response.status_code == 200
#
#
# @pytest.mark.django_db #
# def test_book_view_list(books):
#     client = Client()
#     url = reverse('view_books')
#     response = client.get(url)
#     books_context = response.context['books'] #bv
#     assert books_context.count() == len(books)
#     for b in books:
#         assert b in books_context
#
#
#
# @pytest.mark.django_db
# def test_list_person(books):
#     client = Client()
#     url = reverse('detail_books', args=(books.id,))
#     response = client.get(url)
#     assert books == response.context['book']
#     form = response.context['form']
#     assert isinstance(form, CommentAddForm)