from django import forms
from . view_config import *

class SearchForm(forms.Form):
    searchform = forms.CharField(max_length=20)

class SelectForm(forms.Form):
    choice = []
    choice_list = list(cats_analogue.keys())

    for a in choice_list :
        choice.append((a,a))
        
    selectform = forms.ChoiceField(choices = choice)