from django.contrib import admin

from media.models import Audiobook, Book, Autor, Category, Release
#from media.models import Audiobook

admin.site.register(Audiobook)
admin.site.register(Book)
admin.site.register(Autor)
admin.site.register(Category)
admin.site.register(Release)

