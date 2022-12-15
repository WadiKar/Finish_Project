from multiprocessing.reduction import register

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
        return render(request, '')


class BooksView(View):
    def get(self, request, category=None):
        choose_category = request.GET.get('category')
        if choose_category != '':
            ksiazki = Book.objects.filter(categories__id=choose_category).all()
        else:

            ksiazki = Book.objects.all()
        categories = Category.objects.all()
        bv = {
            'books': ksiazki,
            'categories': categories,
            'choose_category': int(choose_category) if choose_category else None
        }

        return render(request, 'listy2books.html', bv)


class BookDetailView(View):

    def get(self, request, pk):
        ksiazka = Book.objects.get(pk=pk)
        form = BookAddForm()
        return render(request, 'detailbook.html', {'book': ksiazka, 'form':form})


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
            book = Book.objects.create(title=title, year=year)
            book.authors.set(authors)
            book.categories.set(categories)

            return redirect('view_books')
        return render(request, 'form.html', {'form': form})


class ReleasesView(View):
    def get(self, request):
        nowe_posty = Release.objects.all()
        return render(request, 'listy2release.html', {'release': nowe_posty})


class ReleaseDetailView(View):

    def get(self, request, pk):
        released = Release.objects.get(pk=pk)
        return render(request, 'detailrelease.html', {'release': released})


class RelsortView(View):
    def get(self, request, category_release=None):
        choose_category = request.GET.get('date')
        if choose_category != '':
            relacje = Release.objects.filter(category_release__id=choose_category).all()
        else:

            relacje = Release.objects.all()
        category_release = Category.objects.all()
        return render(request, 'listy2release.html', {'release': relacje, 'categories': category_release,
                                                      'choose_category': int(
                                                          choose_category) if choose_category else None})


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
            book = form.cleaned_data['book']
            time = form.cleaned_data['time']
            Audiobook.objects.create(book=book, time=time)
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

# @register.filter
# def sort_lower(lst, fullname):
#     Author.objects.all().extra(select={'lower_name':'LOWER(NAME)'}, order_by='lower_name')
#     return sorted(lst,fullname=lambda item: getattr(item, fullname).lower())
# def filter(self, request):
#     User.objects.annotate(new_field=('first_name')).filter(new_field='Ken')


class AddPostView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.groups.filter(name='Specialist').exists()

    def get(self, request):
        form = ReleaseAddForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = ReleaseAddForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            author_specialist = form.cleaned_data['author_specialist']
            category_release = form.cleaned_data['category_release']
            date = form.cleaned_data['date']
            Release.objects.create(title=title, text=text, author_specialist=author_specialist, category_release=category_release, date=date )

            return redirect('view_release')
        return render(request, 'form.html', {'form': form})
