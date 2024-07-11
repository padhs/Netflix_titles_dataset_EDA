# used oxylabs.io free api to get data from google search

import requests
# from pprint import pprint
import json
import pandas as pd

df = pd.read_csv('./dataset/uncompleted_ntflx_dirs.csv')

# dataframe info
print(df.info())
title = df['title']


def save_to_file(file_name, json_data):
    file_path = f"./ntflx_dirs_queries/{file_name}.txt"
    with open(file_path, 'w') as file:
        json.dump(json_data, file, indent=4)
        # indent 4 is used for pretty print


# creating a dictionary to store the titles which resulted in api call error (error_handling)
keys = ['title']
values = ['error_code']
query_errors = dict(zip(keys, values))


def queries_for_api(param):
    global query_errors
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
            auth=('YOUR_USERNAME', 'YOUR_PASSWORD'),
            json=payload
        )

        # pprint(r.json())
        # let's save the response to a file:
        if r.status_code == 200:
            if '/' in i:
                i = i.replace('/', '_6_9')
                save_to_file(i, r.json())
            else:
                save_to_file(i, r.json())
        elif r.status_code == 500 or r.status_code == 400 or r.status_code == 404:
            print(f'code: {r.status_code}')
            query_errors[i] = str(r.status_code)
        elif r.status_code == 408 or r.status_code == 504:
            print(f'code: {r.status_code} - Request/Gateway Timeout')
            query_errors[i] = str(r.status_code)
        else:
            print('Don\'t know what happened')
            query_errors[i] = str(r.status_code)


queries_for_api(df['title'])
'''
This throws in an error because in index 57, the tile of the movie has a '/' which means a subdirectory
in our set filepath. Since it hasn't been created yet, python can't find it. Need to check for further such characters
Let's replace it with '_6_9'. (a special substring. not likely to be any movie title) Remember to change it later
'''

# find which calls had no results:
print(query_errors)

# Try to run calls again for these:
queries_for_api(query_errors)

# check again which api calls had no results:
print(query_errors)
