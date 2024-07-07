# used oxylabs.io free api to get data from google search

import requests
from pprint import pprint
import json
import pandas as pd

df = pd.read_csv('./dataset/ntflx_without_dirs.csv')

# dataframe info
print(df.info())
title = df['title']


def queries_for_api(param):
    for i in param:
        print(i)
        payload = {
            'source': 'google',
            'url': f'https://www.google.com/search?q={i}'
        }

        '''
        we don't have to include %20 for space character. api can pass on query replacing the space with %20.
        But good coding practices dictate we should include it from our end.
        However, I won't be doing that in order to save time. 
        I might later update this script with proper code practices.
        '''

        r = requests.request(
            'POST',
            'https://realtime.oxylabs.io/v1/queries',
            auth=('bauwa_hqz5Z', '9tVWcBajS62Dr'),
            # put your passkey in 'PASSKEY'
            json=payload
        )

        pprint(r.json())
        # let's save the response to a file:
        if r.status_code == 200:
            file_path = f"./ntflx_dirs_queries/{i}.txt"
            with open(file_path, 'w') as file:
                json.dump(r.json(), file, indent=4)
                # indent 4 is used for pretty print
            if '/' in i:
                i.replace('/', '-')
                file_path = f"./ntflx_dirs_queries/{i}.txt"
                with open(file_path, 'w') as file:
                    json.dump(r.json(), file, indent=4)
                    # indent 4 is used for pretty print


queries_for_api(df['title'])
'''
This throws in an error because in index 57, the tile of the movie has a '/' which means a subdirectory
in our set filepath. Since it hasn't been created yet, python can't find it. Need to check for further such characters
Let's replace it with '-'. Remember to change it later
'''

# invoke api calls for cast as well
