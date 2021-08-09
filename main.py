print("RUN: main.py")
import connectionwifi
import urequests
import json

### je me  connecte a mon point acces
connectionwifi.connect("RasanaPanta","sylvieTchaa1971")

## j' entre mes credential solartracker
username="nomUilisateurde solar"
password="mot de passe solar"
data={"username":username ,"password":password}

### je definis le type de donnees je veu envoyer

requests_headers={
    'content_Type':'application/json'
}

## je fais une premiere tentative de connection pour obtenir le acces_token
request=urequests.post("https://solartracking.herokuapp.com/api/user/login/",json=data,headers=requests_headers)
user=request.json()
access_token=user['access_token']

## je modifie une dernier fois l ' entete pour donner le token access
requests_headers={'content-Type':'application/json' ,'Authorization':'Bearer'+ ' '+access_token}
