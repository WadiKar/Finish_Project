from django.db import models
from django.core.exceptions import ValidationError

from people.models import User


class Author(models.Model):
    fullname = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.fullname


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


def validate_year(value): ## Do czego ona sie tyczy. Jakiej wartosci i jak to mozliwe ze ona działa z tym ponizej
    if value > 2023:
        raise ValidationError("Check year")


class Book(models.Model):
    title = models.CharField(max_length=150)
    year = models.IntegerField(validators=[validate_year])
    authors = models.ManyToManyField(Author, related_name="books")
    categories = models.ManyToManyField(Category)
    relimg = models.ImageField(upload_to='profile_images', default='test.png')

    def __str__(self):
        return self.title


class Audiobook(models.Model):
    time = models.IntegerField()
    authors = models.ManyToManyField(Author, related_name="audiobooks")  # , related_name="audiobooks", through="Book"
    categories = models.ManyToManyField('Category')
    book = models.ForeignKey(Book, blank=False, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.title


class Release(models.Model):
    title = models.TextField(max_length=200)
    text = models.TextField(max_length=2000)
    category_release = models.ForeignKey(Category, on_delete=models.CASCADE)
    author_specialist = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    relimg = models.ImageField(upload_to='profile_images', default='test.png')
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.title, self.date.strftime('%Y-%m-%d %H:%M:%S')}"
