from django.shortcuts import render
import requests
from .forms import CityForm

def weather_view(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=718467f5dcfe1c2e867234b328dbae36'
    city = 'Mumbai'
    error_message = None
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
    else:
        form = CityForm()

    try:
        response = requests.get(url.format(city)).json()
        if response.get('cod') != 200:
            error_message = response.get('message', 'Error fetching data from OpenWeatherMap API')
            weather = None
        else:
            weather = {
                'city': city,
                'temperature': round(response['main']['temp']),
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon']
            }
    except requests.exceptions.RequestException as e:
        error_message = str(e)
        weather = None

    context = {'weather': weather, 'form': form, 'error_message': error_message}
    return render(request, 'weather.html', context)