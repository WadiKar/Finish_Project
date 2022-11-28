from django.contrib import admin

# Register your models here.
from Portal.Media.models import Category, Audiobook, Book, Autor

admin.site.register(Category)
admin.site.register(Audiobook)
admin.site.register(Book)
admin.site.register(Autor)
