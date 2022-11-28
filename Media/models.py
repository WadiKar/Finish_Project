from django.db import models


# Create your models here.
class Autor(models.Model):
    full_name = models.CharField(max_length=128)


class Book(models.Model):
    GRADE = (
        (0, ''),
        (1, '*    '),
        (2, '**   '),
        (3, '***  '),
        (4, '**** '),
        (5, '*****')
    )
    title = models.CharField(max_length=150)
    no_edition = models.IntegerField()
    year = models.IntegerField()
    rating = models.IntegerField(choices=GRADE)
    autors = models.ManyToManyField(Autor, related_name="books", through="Audiobook")
    kategoris = models.ManyToManyField('Category')


class Audiobook(models.Model):
    time = models.IntegerField()
    GRADE = (
        (0, ''),
        (1, '*    '),
        (2, '**   '),
        (3, '***  '),
        (4, '**** '),
        (5, '*****')
    )

    opinion = models.IntegerField(choices=GRADE)
    autors = models.ManyToManyField(Autor, related_name="audiobooks", through="Book")
    kateg = models.ManyToManyField('Category')
    book = models.ForeignKey(Book, blank=True, null=True, on_delete=models.CASCADE, )


class Category(models.Model):
    name = models.CharField(max_length=64)
