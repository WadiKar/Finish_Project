
from django.db import models
# Create your models here.
from people.models import Specialist


class Autor(models.Model):
    full2name = models.CharField(max_length=128, null=True)


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
    autors = models.ManyToManyField(Autor) #, related_name="books", through="Audiobook"
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
    autors = models.ManyToManyField(Autor) #, related_name="audiobooks", through="Book"
    kateg = models.ManyToManyField('Category')
    book = models.ForeignKey(Book, blank=True, null=True, on_delete=models.CASCADE, )



class Category(models.Model):
    name = models.CharField(max_length=64)

    # class Mate:
    #     verbose_name = "Category"
    #     verbose_name_plural = "Kategorie"

class Release(models.Model):
    text = models.TextField()
    category_release = models.ForeignKey(Category, on_delete=models.CASCADE)
    author_specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    models.ImageField(upload_to='profile_images', default='new_post.png')
    date = models.DateTimeField(auto_now_add=True)

    # class Mate:
    #     verbose_name = "Release"
    #     verbose_name_plural = "Nowy Post"
