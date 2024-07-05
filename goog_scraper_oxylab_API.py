# used oxylabs.io free api to get data from google search

import requests
from pprint import pprint
import json

queries = ['Kota', 'Factory']

payload = {
    'source': 'google',
    'url': f'https://www.google.com/search?q={queries[0]}%20{queries[1]}'
    '''
        we don't have to include %20 for space character. api can pass on query replacing the space with %20.
        But good coding practices dictate we should include it from our end.
        However, I won't be doing that in order to save time. 
        I might later update this script with proper code practices.
    '''
}

r = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('bauwa_hqz5Z', '9tVWcBajS62Dr'),
    # put your passkey in 'PASSKEY'
    json=payload
)

pprint(r.json())
# let's save the response to a file:
file_path = f"./temp_dir_files/{queries[0]}_{queries[1]}.txt"
with open(file_path, 'w') as file:
    json.dump(r.json(), file, indent=4)
    # indent 4 is used for pretty print

