from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import DetailView

from media.forms import ReleaseAddForm, BookAddForm, AuthorAddFrom, AudiobookAddForm
from media.models import Book, Category, Audiobook, Release, Author
from people.models import User


class IndexView(View):

    def get(self, request):
        return render(request, 'klu')


class BooksView(View):
    def get(self, request):
        ksiazki = Book.objects.all()
        return render(request, 'listy2.html', {'books': ksiazki})


class BookDetailView(View):

    def get(self, request, pk):
        ksiazka = Book.objects.get(pk=pk)
        return render(request, 'detailbook.html', {'book': ksiazka})


class AddBookView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.groups.filter(name='Specialist').exists()

    def get(self, request):
        form = BookAddForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = BookAddForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            year = form.cleaned_data['year']
            authors = form.cleaned_data['authors']
            categories = form.cleaned_data['categories']
            Book.objects.create(title=title, year=year, authors=authors, categories=categories)
            return redirect('/')
        return render(request, 'form.html', {'form': form})


class ReleasesView(View):
    def get(self, request):
        nowe_posty = Audiobook.objects.all()
        return render(request, 'listaudiobooks.html', {'release': nowe_posty})


class AudiobookDetailView(View):

    def get(self, request, pk):
        nowy_post = Audiobook.objects.get(pk=pk)
        return render(request, 'detailrelease.html', {'new_post': nowy_post})



class AudiobooksView(View):
    def get(self, request):
        audiobuki = Audiobook.objects.all()
        return render(request, 'listy2audiobooks.html', {'audiobooks': audiobuki})


class AudiobookDetailView(View):

    def get(self, request, pk):
        audiobuks = Audiobook.objects.get(pk=pk)
        return render(request, 'detailaudiobook.html', {'audiobooks': audiobuks})


class AddAudiobookView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.groups.filter(name='Specialist').exists()

    def get(self, request):
        form = AudiobookAddForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AudiobookAddForm(request.POST)
        if form.is_valid():
            # title = form.cleaned_data['title']
            # time = form.cleaned_data['time']
            # Book.objects.create(title=title, time=time)
            return redirect('/')
        return render(request, 'form.html', {'form': form})


class CreateAuthorView(View):
    def test_func(self):
        return self.request.user.groups.filter(name='Specialist').exists()

    def get(self, request):
        return render(request, 'create_author.html')

    def post(self, request):
        fullname = request.POST.get('fullname')
        Author.objects.create(fullname=fullname)
        return redirect('view_author')


class AuthorView(View):
    def get(self, request):
        autorzy = Author.objects.all()
        return render(request, 'listy2authors.html', {'authors': autorzy})


class AuthorDetailView(View):

    def get(self, request, pk):
        autorzy = Author.objects.get(pk=pk)
        return render(request, 'detailauthor.html', {'author': autorzy})
