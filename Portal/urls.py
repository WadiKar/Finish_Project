"""Portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from people.views import LogoutView, RegisterView, LoginView, SpecialistView, SpecialistDetailView, MyView, \
    Make_appointment, Detail_appointment, VisitView, VisitForCompanyView
from media.views import BooksView, AudiobooksView, BookDetailView, AudiobookDetailView, AddBookView, \
    AuthorView, CreateAuthorView, AuthorDetailView, AuthorView, AddAudiobookView, ReleaseDetailView, \
    RelsortView, ReleasesView, AddPostView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', TemplateView.as_view(template_name='base.html'), name='index'),
                  path('logout/', LogoutView.as_view(), name='logout'),
                  path('register/', RegisterView.as_view(), name='register'),
                  path('login/', LoginView.as_view(), name='login'),

                  path('books/', BooksView.as_view(), name='view_books'),
                  path('books/<int:pk>/', BookDetailView.as_view(), name='detail_books'),
                  path('addBook/', AddBookView.as_view(), name='create_book'),

                  path('audiobooks/', AudiobooksView.as_view(), name='view_audiobooks'),
                  path('audiobooks/<int:pk>/', AudiobookDetailView.as_view(), name='detail_audiobook'),
                  path('createaudiobook/', AddAudiobookView.as_view(), name='create_audiobook'),

                  path('releases/', ReleasesView.as_view(), name='view_release'),
                  path('releases/<int:pk>/', ReleaseDetailView.as_view(), name='detail_release'),
                  path('create_release/', AddPostView.as_view(), name='create_release'),
                  path('releasessort/', RelsortView.as_view(), name='view_releasesort'),

                  path('authors/', AuthorView.as_view(), name='view_author'),
                  path('createauthor/', CreateAuthorView.as_view(), name='create_author'),
                  path('authors/<int:pk>/', AuthorDetailView.as_view(), name='detail_author'),

                  path('specialists/', SpecialistView.as_view(), name='view_specialist'),
                  path('specialists/<int:pk>/', SpecialistDetailView.as_view(), name='detail_specialists'),
                  path('myview/', MyView.as_view(), name='myview'),

                  path('make_appointment/', Make_appointment.as_view(), name='make_appointment'),
                  path('detail_appointment/<int:pk>/', Detail_appointment.as_view(), name='detail_appointment'),
                  path('appointment/', VisitView.as_view(), name='view_appointment'),

                  path('company/', VisitForCompanyView.as_view(), name='view_company'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
