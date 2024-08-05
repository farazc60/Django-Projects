from django.shortcuts import render
from .forms import TextInputForm
from collections import Counter
from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0


def home(request):
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            word_count = len(text.split())
            reversed_text = text[::-1]
            uppercase_text = text.upper()
            lowercase_text = text.lower()
            titlecase_text = text.title()

            # Frequency Analysis
            words = text.split()
            frequency = dict(Counter(words))

            # Text Summary (Extracting first 3 sentences)
            sentences = text.split('. ')
            summary = '. '.join(sentences[:3]) if len(sentences) > 3 else text

            # Language Detection
            try:
                language = detect(text)
            except:
                language = "Unable to detect"

            return render(request, 'results.html', {
                'form': form,
                'word_count': word_count,
                'reversed_text': reversed_text,
                'uppercase_text': uppercase_text,
                'lowercase_text': lowercase_text,
                'titlecase_text': titlecase_text,
                'frequency': frequency,
                'summary': summary,
                'language': language,
            })
    else:
        form = TextInputForm()
    return render(request, 'home.html', {'form': form})
