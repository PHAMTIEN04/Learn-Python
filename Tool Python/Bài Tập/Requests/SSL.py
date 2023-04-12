# import requests

# s =requests.session()
# s.verify = 'path/to/CAs'

# r = s.get('https://github.com')
import requests

s = requests.session()
s.verify = 'path/to/CAs'

r = s.get('https://github.com')

