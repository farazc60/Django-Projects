from django.shortcuts import render
from .forms import BMIForm

def bmi_calculator(request):
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            bmi = weight / (height ** 2)
            return render(request, 'bmi_result.html', {'bmi': bmi})
    else:
        form = BMIForm()
    return render(request, 'bmi_form.html', {'form': form})