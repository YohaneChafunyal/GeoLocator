from django import forms
from .models import Search


class SearchForm(forms.ModelForm):
    destination = forms.CharField(label='destination:')
    address = forms.CharField(label='source:')

    class Meta:
        model = Search
        fields = ['address', ]
        fields = ['destination']
