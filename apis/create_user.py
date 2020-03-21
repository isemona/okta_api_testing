"""Script to create a user from the Okta User API"""

import json, requests

api_token = 'your api token here'
api_url_base = 'https://example.oktapreview.com/api/v1/users'

headers = {'Content-Type': 'application/json',
           'Authorization': 'SSWS {0}'.format(api_token)}
# Get User Info
def create_account():

#     api_url = '{0}'.format(api_url_base)
    payload = {
      "profile": {
        "firstName": "Saml",
        "lastName": "Jackson",
        "email": "saml.jackson@oktapreview.com",
        "login": "saml.jackson@oktapreview.com"
      }
    }
    response = requests.post(api_url_base, data=json.dumps(payload), headers=headers)
#     print(response.txt)
    response_json = response.json()
    print(response_json)

    create_account()