from django.shortcuts import render
from .forms import ConversionForm
from decimal import Decimal, ROUND_HALF_UP
import requests

def convert_currency(amount, from_currency, to_currency):
    # Fetch exchange rate from API
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    # Get the exchange rate for the target currency
    rate = data['rates'].get(to_currency, 1)

    # Convert rate to Decimal if it's a float
    if isinstance(rate, float):
        rate = Decimal(rate)

    # Convert amount to Decimal
    amount_decimal = Decimal(amount)
    converted_amount = amount_decimal * rate

    # Round to 2 decimal places
    converted_amount = converted_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    return converted_amount

def home(request):
    result = None
    if request.method == 'POST':
        form = ConversionForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            from_currency = form.cleaned_data['from_currency']
            to_currency = form.cleaned_data['to_currency']
            converted_amount = convert_currency(amount, from_currency, to_currency)
            result = f"{to_currency} {converted_amount}"
    else:
        form = ConversionForm()
    return render(request, 'home.html', {'form': form, 'result': result})