# this script doesn't work. bs4 cannot retrieve dynamically loaded data

import requests
from bs4 import BeautifulSoup
from pprint import pprint

# URL of the page to scrape
url = 'https://www.google.com/search?q=Kota%20Factory'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div element with aria-label="About"
    #about_div = soup.find('div', {'Class': 'TzHB6b Hwkikb WY0eLb EqrSYc'})
    about_div = soup.find_all('div', {'class': 'TzHB6b Hwkikb WY0eLb EqrSYc'})

    # Check if the div was found
    if about_div:
        # Print the text content of the div
        print(about_div.get_text(strip=True))
        # pprint(about_div.json())
    else:
        print('Div element with aria-label="About" not found.')
        # it cannot find the element because elements and data is being dynamically loaded. better to use api
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
