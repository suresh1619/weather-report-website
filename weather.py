import requests

api_key = '668af2db3004485c92074505250601'
city = 'sattenapalle'
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'

response = requests.get(url)
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")
