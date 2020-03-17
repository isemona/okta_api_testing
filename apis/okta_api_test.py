# import json
# import requests


# api_token = '00l-98rUxuBYotnn-DfJF9kuI79PWMxonN7ItRnPOX'
# api_url_base = 'https://semonav2.oktapreview.com/api/v1/users'


# headers = {'Content-Type': 'application/json',
#            'Authorization': 'Bearer {0}'.format(api_token)}


# def get_account_info():

#     api_url = '{0}users'.format(api_url_base)

#     response = requests.get(api_url, headers=headers)

#     if response.status_code == 200:
#         return json.loads(response.content.decode('utf-8'))
#     else:
#         return None

# account_info = get_account_info()

# print(account_info)
# if account_info is not None:
#     print("Here's your info: ")
#     for k, v in account_info['account'].items():
#         print('{0}:{1}'.format(k, v))

# else:
#     print('[!] Request Failed')



from okta import UsersClient
# http://developer.okta.com/docs/api/getting_started/getting_a_token.html
usersClient = UsersClient('https://example.oktapreview.com/',
                          '01a2B3Cd4E5fGHiJ6K7l89mNOPQRsT0uVwXYZA1BCd')


from okta import UsersClient
# http://developer.okta.com/docs/api/getting_started/getting_a_token.html
usersClient = UsersClient('https://example.oktapreview.com/',
                          '01a2B3Cd4E5fGHiJ6K7l89mNOPQRsT0uVwXYZA1BCd')

new_user = User(login='example@example.com',
                email='example@example.com',
                firstName='Saml',
                lastName='Jackson')
user = usersClient.create_user(new_user, activate=False)

