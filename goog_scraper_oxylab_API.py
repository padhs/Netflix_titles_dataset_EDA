import requests
from pprint import pprint

payload = {
    'source': 'google',
    'url': 'https://www.google.com/search?q=Kota%20Factory'
}

r = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('bauwa_hqz5Z', '9tVWcBajS62Dr'),
    json=payload
)

pprint(r.json())
