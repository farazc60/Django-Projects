from django import forms

class TranslationForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Text to Translate')
    target_language = forms.ChoiceField(choices=[('en', 'English'), ('fr', 'French'), ('de', 'German'), ('es', 'Spanish')], label='Target Language')
