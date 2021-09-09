import requests

url = "https://random-data-api.com/api/internet_stuff/random_internet_stuff"

reponse = requests.get(url)
contenu = reponse.json()
print(contenu.id)