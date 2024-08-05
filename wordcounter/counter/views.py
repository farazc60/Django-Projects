from django.shortcuts import render
from .forms import TextInputForm


def count_words(request):
    word_count = None
    form = TextInputForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data['text']
        word_count = len(text.split())

    return render(request, 'count_words.html', {'form': form, 'word_count': word_count})
