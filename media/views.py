from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views import View
from media.forms import ReleaseAddForm, BookAddForm, AuthorAddFrom, AudiobookAddForm
from media.models import Book, Category, Audiobook, Release, Author


class IndexView(View):
    """ Strona główna dla niezalogowanych i zalogowanych z całym menu do wyboru"""

    def get(self, request):
        return render(request, '')


class BooksView(View):
    """
    Widok ksiażek, całej listy. z filtrowaniem. Jesli jest wskazana katagoria, to wyświetlają ksiazki, ktore sa przepisane do id które jest oznaczone poprzez !=''
    A na koniec warunek że jesli caktegoria nie jest wybrana to nie jest nic wyswietlany i jest to widok na  start
    """
    def get(self, request, category=None):
        choose_category = request.GET.get('category')
        if choose_category != '':
            ksiazki = Book.objects.filter(categories__id=choose_category).all()
        else:

            ksiazki = Book.objects.all()
        #ksiazki = Book.objects.all()
        categories = Category.objects.all()
        bv = {
            'books': ksiazki,
            'categories': categories,
            'choose_category': int(choose_category) if choose_category else None
        }
        return render(request, 'listy2books.html', bv)


class BookDetailView(View):
    """
        Wyswietlane są szczegóły ksiązki. uzywa formularza. Szczegóły wyświetlają się po podaniu id książki.
        """
    def get(self, request, pk):
        ksiazka = Book.objects.get(pk=pk)
        form = BookAddForm()
        return render(request, 'detailbook.html', {'book': ksiazka, 'form': form})


class AddBookView(UserPassesTestMixin, View):
    """
    Widok dodawania książki z uprawnieniem że użytkownik jest specjalistą.
    W metodzie POST funkcja sprawdza czy podne wartości są zgodne z wartościami zadeklarowanymi w models.py
    """
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
    """ Widok listy wszystkich postów które dodał specjalista"""
    def get(self, request):
        nowe_posty = Release.objects.all()
        return render(request, 'listy2release.html', {'release': nowe_posty})


class ReleaseDetailView(View):
    """Szczegóły relacji lub postów które dodał specjalista"""

    def get(self, request, pk):
        released = Release.objects.get(pk=pk)
        return render(request, 'detailrelease.html', {'release': released})




class AudiobooksView(View):
    """Lista audibooków dodanych przez admina lub specjalistę. Do wglądu dla pracownika lub pacjenta. """
    def get(self, request):
        audiobuki = Audiobook.objects.all()
        return render(request, 'listy2audiobooks.html', {'audiobooks': audiobuki})


class AudiobookDetailView(View):
    """Szczegóły audiobooka, czas trwania, tytuł książki i kategorii"""

    def get(self, request, pk):
        audiobuks = Audiobook.objects.get(pk=pk)
        form = AudiobookAddForm()
        return render(request, 'detailaudiobook.html', {'audiobooks': audiobuks, 'form': form})



class AddAudiobookView(UserPassesTestMixin, View):
    """
      Widok dodawania audiobooka z uprawnieniem że użytkownik jest specjalistą.
      W metodzie POST funkcja sprawdza czy podne wartości są zgodne z wartościami zadeklarowanymi w models.py
      """

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
    """
      Widok dodawania autora z uprawnieniem że użytkownik jest specjalistą.
      W metodzie POST funkcja tworzy nowy obiekt
      """
    def test_func(self):
        return self.request.user.groups.filter(name='Specialist').exists()

    def get(self, request):
        return render(request, 'create_author.html')

    def post(self, request):
        fullname = request.POST.get('fullname')
        Author.objects.create(fullname=fullname)
        return redirect('view_author')


class AuthorView(View):
    "Lista autorów dodanych przez admina lub specjalistę. Do wglądu dla pracownika lub pacjenta. """
    def get(self, request):
        autorzy = Author.objects.all()
        return render(request, 'listy2authors.html', {'authors': autorzy})


class AuthorDetailView(View):
    """Szczegóły autora. Napisane książki. URL działa z podaniem id książki"""
    def get(self, request, pk):
        autorzy = Author.objects.get(pk=pk)
        return render(request, 'detailauthor.html', {'author': autorzy})


class AddPostView(UserPassesTestMixin, View):
    """
         Widok dodawania relacji z uprawnieniem że użytkownik jest specjalistą.
         W metodzie POST funkcja sprawdza czy podne wartości są zgodne z wartościami zadeklarowanymi w models.py
        i tworzy nowy obiekt
         """
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
            Release.objects.create(title=title, text=text, author_specialist=author_specialist,
                                   category_release=category_release, date=date)

            return redirect('view_release')
        return render(request, 'form.html', {'form': form})
