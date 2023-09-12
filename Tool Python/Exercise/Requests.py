import requests

# demo 1 => requests get
url = 'https://api.github.com'
reponse = requests.get(url)
print(reponse.text)