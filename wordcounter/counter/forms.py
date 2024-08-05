from django import forms

class TextInputForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 40, 'placeholder': 'Enter your text here...'}), label='')
