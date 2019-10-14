from django.forms import ModelForm
from .models import Produkt
from django import forms

class DrugIntCheckForm(forms.Form):
    check_drug = forms.CharField(label= '', max_length=150,
        widget=forms.TextInput(attrs={'placeholder':
        'Geben Sie ein Medikament ein...'}))
