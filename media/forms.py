from django import forms

from media.models import Release


class ReleaseAddForm(forms.ModelForm):

    class Meta:
        model = Release
        fields = ['text'] # okreslenie ;formatu' Comment