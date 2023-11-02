import json
import requests

print("Please enter your zip code: ")
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=934ff61d5074287fff0ffcf252e3f3c4' % zip)
data = r.json()
print(data['weather'][0]['description'])