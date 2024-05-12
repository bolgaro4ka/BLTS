from django import forms
from .models import Test, Task, Answer_from_user

class TestSmallForm(forms.Form):
    answer=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ответ', 'id': 'answer'}), label='')

