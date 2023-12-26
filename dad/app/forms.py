from django import forms
from .models import *

class BookForm(forms.Form):
    class Meta(forms.Form):
        model = Book
        # fields = ['name', 'author']
        fields = '__all__'

class AuthorForm(forms.Form):
    class Meta(forms.Form):
        model = Author
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Имя'})
        }

