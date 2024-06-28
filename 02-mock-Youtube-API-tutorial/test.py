import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + 'helloworld/' + "nicholas/" + "23")

print(response.json())