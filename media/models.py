from django.db import models

from people.models import User


class Autor(models.Model):
    fullname = models.CharField(max_length=128, null=True)
    def __str__(self):
        return self.fullname

class Book(models.Model):
    # GRADE = (
    #     (0, ''),
    #     (1, '*    '),
    #     (2, '**   '),
    #     (3, '***  '),
    #     (4, '**** '),
    #     (5, '*****')
    # )
    title = models.CharField(max_length=150)
    year = models.IntegerField()
    # rating = models.IntegerField(choices=GRADE)
    autors = models.ManyToManyField(Autor, )  # , related_name="books", through="Audiobook"
    kategoris = models.ManyToManyField('Category')

    def __str__(self):
        return self.title


# self.auttors
class Audiobook(models.Model):
    time = models.IntegerField()
    # GRADE = (
    #     (0, ''),
    #     (1, '*    '),
    #     (2, '**   '),
    #     (3, '***  '),
    #     (4, '**** '),
    #     (5, '*****')
    # )
    #
    # opinion = models.IntegerField(choices=GRADE)
    autors = models.ManyToManyField(Autor, related_name="audiobooks")  # , related_name="audiobooks", through="Book"
    kategoris = models.ManyToManyField('Category')
    book = models.ForeignKey(Book, blank=False, null=True, on_delete=models.CASCADE, )
    def __str__(self):
        return self.book

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Release(models.Model):
    text = models.TextField(max_length=1200)
    category_release = models.ForeignKey(Category, on_delete=models.CASCADE)
    author_specialist = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    relimg = models.ImageField(upload_to='profile_images', default='new_post.png')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author_specialist
