import requests

api_key = '#################'
city = 'sattenapalle'
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'

response = requests.get(url)
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")
