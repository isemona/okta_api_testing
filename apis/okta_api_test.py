"""Helper functions used to get and create users"""

import json
import requests

api_token = 'your api token here'
api_url_base = 'https://example.oktapreview.com/'

headers = {'Content-Type': 'application/json',
           'Authorization': 'SSWS {0}'.format(api_token)}

# Get User Info
def get_account_info():

    api_url = '{0}'.format(api_url_base)

    response = requests.get(api_url, headers=headers)

    # using f-strings here; much faster (yay!) and easier to read than formatting strings!
    # print(f"Got response: {response}")
    # print(f"Got response.content: {response.content}")

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        # Can explicitly return None here to mean "an error happened"
        return {}

account_info = get_account_info()





