from django import forms


class NmapForm(forms.Form):
    ip = forms.CharField(max_length=50, label='ip')