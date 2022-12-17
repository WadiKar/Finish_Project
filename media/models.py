from django.db import models
from django.core.exceptions import ValidationError

from people.models import User


class Author(models.Model):
    """
    Model autor z wartoscią tylko nazwika
    """
    fullname = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.fullname


class Category(models.Model):
    """
      Model kategorii z wartoscią nazwy kategorii
    """
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


def validate_year(value):  ## Do czego ona sie tyczy. Jakiej wartosci i jak to mozliwe ze ona działa z tym ponizej
    if value > 2023:
        raise ValidationError("Check year")


class Book(models.Model):
    """
    Model wykorzytujacy funkcje zablokowania daty do przodu.
    Zawiera tytuł (nazwe ksiażki), rok wydania, autora ktory ma relację M2M. A także categories, bedąca relacją M2M poniewaz ksiazka moze miec wiele kategorii i wiele kategorii może mieć wiele książek.
    Oraz zdjecie okładki, wyswietlana tylko przy liście książki.
    """
    title = models.CharField(max_length=150)
    year = models.IntegerField(validators=[validate_year])
    authors = models.ManyToManyField(Author, related_name="books")
    categories = models.ManyToManyField(Category)
    relimg = models.ImageField(upload_to='profile_images', default='test.png')

    # relimg, year, title,  categories, authors,
    def __str__(self):
        return f"{self.title}, {self.year}, {self.relimg}"


class Audiobook(models.Model):
    """
    Model potrzebuje wartość czasu trwania audiobooka, autora ktory ma relacje M2M oraz categorie, również z relacją M2M. Oraz potrzebuje nazwy ksiązki, czyli relacja Foreinkey do ksiązki.
    """
    time = models.IntegerField()
    authors = models.ManyToManyField(Author, related_name="audiobooks")  # , related_name="audiobooks", through="Book"
    categories = models.ManyToManyField('Category')
    book = models.ForeignKey(Book, blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.title


class Release(models.Model):

    """
    Model który potrzebuje tytuł postu, całkowita treśc informacji, categorii oraz autorów ktrorzy mają relację ForeinKey. Do tego obraz który jest ustawiony domyślny,
    oraz datę z formatem '2020-11-23 12:45'
    """
    title = models.TextField(max_length=200)
    text = models.TextField(max_length=2000)
    category_release = models.ForeignKey(Category, on_delete=models.CASCADE)
    author_specialist = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    relimg = models.ImageField(upload_to='profile_images', default='test.png')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title, self.date.strftime('%Y-%m-%d %H:%M:%S')}"
