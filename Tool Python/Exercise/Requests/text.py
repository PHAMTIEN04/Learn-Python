import requests

url = "https://www.facebook.com/profile.php?id=100050801498135"
rq = requests.get(url= url )
print(rq.text)