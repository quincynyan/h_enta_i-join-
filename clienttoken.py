import requests

import requests.auth

import configparser
config = configparser.ConfigParser()
config.read('token.ini')

client_auth = requests.auth.HTTPBasicAuth(
    config['reddit']['client_id'], config['reddit']['client_secret'])

post_data = {"grant_type": "password",
             "username": config["reddit"]["username"], "password": config["reddit"]["password"]}

headers = {"User-Agent": "web:www_flairbot:v1.0.0 (by /u/ironohki)"}

response = requests.post("https://www.reddit.com/api/v1/access_token",
                         auth=client_auth, data=post_data, headers=headers)

response.json()

print(response.json())
