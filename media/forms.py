from django import forms

from media.models import Release, Book, Category
from people.models import User


class BookAddForm(forms.Form):
    title = forms.CharField(max_length=150)
    year = forms.IntegerField()
    autors = forms.ModelMultipleChoiceField(queryset=Book.objects.all(), widget=forms.CheckboxSelectMultiple())
    kategoris = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple())


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