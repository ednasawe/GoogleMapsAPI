import requests

api_address = 'https://api.openweathermap.org/data/2.5/weather?APPID=47dcc1650027ba13eaefb7411c44aab6&q='
city = input("City Name:")

url = api_address + city
open_file = url
self = city

json_data = requests.get(url).json()
formatted_data = json_data['weather'][0]['description']

print(formatted_data)
