import requests
import json

r = requests.get('http://localhost:3000')

if r.status_code == 200:
    widgets = r.json()
    for widget in widgets:
        print(widget['name'] + " is " + widget['color'] + ".")
else:
    print(f"Failed to retrive widgets from web server, the corresponding response code: {r.status_code}")