# translator/views.py
from django.shortcuts import render
from googletrans import Translator
from .forms import TranslationForm

def translate_text(request):
    translation = None
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            target_language = form.cleaned_data['target_language']
            translator = Translator()
            translation = translator.translate(text, dest=target_language)
    else:
        form = TranslationForm()
    return render(request, 'translate.html', {'form': form, 'translation': translation})