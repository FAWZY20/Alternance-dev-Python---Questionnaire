import requests

url = "https://random-data-api.com/api/internet_stuff/random_internet_stuff"

reponse = requests.get(url)
contenu = reponse.json()

username = contenu['username']
email = contenu['email']

print("L'adresse email de l'utilisateur " + username + " est " + email)