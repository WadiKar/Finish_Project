from django.contrib import admin

from media.models import Audiobook, Book, Author, Category, Release
#from media.models import Audiobook

admin.site.register(Audiobook)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Release)

