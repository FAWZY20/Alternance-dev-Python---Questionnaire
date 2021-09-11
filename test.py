import requests

url = "https://random-data-api.com/api/internet_stuff/random_internet_stuff"

reponse = requests.get(url)
contenu = reponse.json()
username = contenu['username']
email = contenu['email']
os = contenu['user_agent']
windows = os.count('Windows')
Linux = os.count('Linux')
MacOS = os.count('Macintosh')
Android = os.count('Android')

if(username != None or email != None):

    if windows == 1:

        os_emojie = "Windows"

    elif Linux == 1:

        os_emojie = "Linux"

    elif MacOS == 1:

        os_emojie = "MacOS"

    elif Android == 1:

        os_emojie = "Android"

    else:
        os_emojie = "Aucun OS reonnut"

else:

    print("aucun user est reconnu")


print("L'adresse email de l'utilisateur " + username + " est " + email +
      " ." + " Iel utilise le système d'exploitation " + os_emojie + " . ")