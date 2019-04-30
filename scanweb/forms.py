from django import forms
from .models import Scanweb


class WebForm(forms.ModelForm):
    url = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = Scanweb
        fields = [
            'url',
            'title',
        ]




