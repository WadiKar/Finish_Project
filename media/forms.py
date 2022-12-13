from django import forms
from wtforms import ValidationError

from media.models import Release, Book, Category, Author, Audiobook
from people.models import User


class BookAddForm(forms.Form):
    title = forms.CharField(max_length=150)
    year = forms.IntegerField()
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all(), widget=forms.CheckboxSelectMultiple())
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple())

    def clean(self):
        cleaned_data = super().clean()  ## wykorzystuje metody z min-year czy movieadd
        return cleaned_data

# class ReleaseAddForm(forms.Form):
#     text = forms.TextField()
#     category_release = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
#     author_specialist = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.RadioSelect)
#     relimg = forms.ImageField()  # (upload_to='profile_images', default='new_post.png')
#     date = forms.DateTimeField(auto_now_add=True, format='%Y-%m-%d')

class ReleaseAddForm(forms.Form):
    class Meta:
        model = Release
        fields = ['text']


class AuthorAddFrom(forms.Form):
    fullname = forms.CharField(max_length=128)

    class Meta:
        model = Author
        fields = ['fullname']



class AudiobookAddForm(forms.Form):
    time = forms.CharField()
    book = forms.ModelChoiceField(queryset=Audiobook.objects.all(), widget=forms.RadioSelect)


