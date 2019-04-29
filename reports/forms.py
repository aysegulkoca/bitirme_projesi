from django import forms

from .models import Report


class ReportForm(forms.ModelForm):
    ip = forms.CharField(widget=forms.TextInput(
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
        model = Report
        fields = [
            'ip',
            'title',
        ]