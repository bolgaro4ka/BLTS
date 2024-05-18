from django import forms
from .models import Test, Task, Answer_from_user

class TestSmallForm(forms.Form):
    answer=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ответ', 'id': 'answer'}), label='')

class TestBigForm(forms.Form):
    answer=forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ответ', 'id': 'answer'}), label='')

class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Поиск', 'id': 'search'}), label='', required=False)