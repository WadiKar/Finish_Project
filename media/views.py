from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from media.forms import ReleaseAddForm, BookAddForm
from media.models import Book, Category, Audiobook, Release, Autor
from people.models import User


class IndexView(View):

    def get(self, request):
        return render(request, 'klu')


class BooksView(View):
    def get(self, request):
        ksiazki = Book.objects.all()
        return render(request, 'listbook.html', {'books': ksiazki})


class AudiobooksView(View):
    def get(self, request):
        audiobuki = Audiobook.objects.all()
        return render(request, 'listaudiobooks.html', {'audiobooks': audiobuki})


class ReleasesView(View):
    def get(self, request):
        nowe_posty = Audiobook.objects.all()
        return render(request, 'listaudiobooks.html', {'release': nowe_posty})


class BookDetailView(View):

    def get(self, request, pk):
        ksiazka = Book.objects.get(pk=pk)
        return render(request, 'detailbook.html', {'movie': ksiazka})


class AudiobookDetailView(View):

    def get(self, request, pk):
        audiobuks = Audiobook.objects.get(pk=pk)
        return render(request, 'detailaudiobook.html', {'audiobook': audiobuks})


# class ReleasesDetailView(View):
#     def get(self, request, pk):
#         nowy_post = Release.objects.get(pk=pk)
#         return render(request, 'detailrelease.html', {'release': nowy_post})
# def releasesDetailView(request, pk):
#
#     nowy_post = Release.objects.get(pk=pk)
#     form = ReleaseAddForm()
#     return render(request, 'detailrelease.html', {'release': nowy_post, 'form': form})

class AddBookView(PermissionRequiredMixin, View):
    permission_required = ['media.add_book']

    def get(self, request):
        form = BookAddForm()  #
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = BookAddForm(request.POST)  #
        if form.is_valid():
            title = form.cleaned_data['title']
            year = form.cleaned_data['year']
            autors = form.cleaned_data['autors']
            kategoris = form.cleaned_data['kategoris']
            Book.objects.create(title=title, year=year,
                                 autors=autors, kategoris=kategoris)
            return redirect('/')
        return render(request, 'form.html', {
            'form': form})


class CreateAutorView(View):

    def get(self, request):
        return render(request, 'addAuthor.tml')

    def post(self, request):
        imie = request.POST.get('first_name')
        nazwisko = request.POST.get('last_name')
        Autor.objects.create(first_name=imie, last_name=nazwisko)
        return redirect('list_person')


class ListAutorView(View):
    def get(self, request):
        autorzy = Autor.objects.all()
        return render(request, 'listauthor.html', {'authors': autorzy})