"""Script to create multiple users from the Okta User API"""

import json, requests

from faker import Faker 

api_token = 'your api token here'
api_url_base = 'https://example.oktapreview.com/api/v1/users'

headers = {'Content-Type': 'application/json',
           'Authorization': 'SSWS {0}'.format(api_token)}

fake = Faker() 
def input_data(x): 
    for _ in range(0, x):
      user_info = {
        "profile": {
          "firstName": fake.first_name(),
          "lastName": fake.last_name(),
          "email": fake.email(),
          "login": fake.email()  
        }
      }    
      response = requests.post(api_url_base, data=json.dumps(user_info), headers=headers)  
      response_json = response.json()
      print(response_json)

input_data(30)