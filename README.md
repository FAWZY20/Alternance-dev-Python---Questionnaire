1. appelle le point d'accès [`https://random-data-api.com/api/internet_stuff/random_internet_stuff`](https://random-data-api.com/api/internet_stuff/random_internet_stuff) 

2. imprime dans la console le message suivant:

`L'adresse email de l'utilisateur {username} est {adresse email}. Iel utilise le système d'exploitation {os emoji}.`

Dans ce message, les termes entre `{}` doivent être remplacés par les paramètres suivants, en fonction de la réponse de l'API:

- `username`: `username`
- `adresse email`: `email`
- `os emoji`:
    - Si le système d'exploitation est Windows: 🪟
    - Si le système d'exploitation est Linux: 🐧
    - Si le système d'exploitation est MacOs ou iOS: 🍎
    - Si le système d'exploitation est Android: 🤖

exemple: `L'adresse email de l'utilisateur Jeanpetit23 est jean@petit.be. Iel utilise le système d'exploitation` 🍎`.`

N'oublie pas de gérer les cas ou l'API retournerait une erreur.
