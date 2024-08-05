from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border-2 p-2 border-gray-300 shadow-sm',
                'placeholder': 'Enter the book title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-md border-2 p-2 border-gray-300 shadow-sm',
                'placeholder': 'Enter the author name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea resize-none mt-1 block w-full rounded-md border-2 p-2 border-gray-300 shadow-sm',
                'rows': 4,
                'placeholder': 'Enter a brief description of the book'
            }),
        }