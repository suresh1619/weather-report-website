import requests
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

def weather_view(request):
    city = request.GET.get('city', 'Sattenapalle')  # Default to 'Sattenapalle' if no city is provided
    api_key = settings.WEATHER_API_KEY
    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&aqi=no'

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()

        return render(request, 'weather.html', {'weather_data': weather_data, 'city': city})
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return HttpResponse("Failed to fetch weather data. Please try again later.", status=500)
