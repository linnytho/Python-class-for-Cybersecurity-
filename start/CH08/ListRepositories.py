#!/usr/bin/env python3
# Script that lists repositories in GitHub
# Requires a Personal Access Token to run
# By 
import os
import configparser

def get_api_key(key_name):
    # Get the location of the secrets file
    home_dir = os.path.expanduser("~")
    secret_file = os.path.join(home_dir, "secret.ini")
    #Creat configparser and load file
    config = configparser.ConfigParser()
    config.read(secret_file)
    #Get API key and return 
    api_key = config["APIKeys"][key_name]
    return api_key


#token = get_api_key("github")
#print(token)

import requests
def get_repositories(token):
    url = "https://api.github.com/user/repos"
    headers = {"Authorization": "Bearer " + token}
    response = requests.get(url, headers=headers)
    return response.json()

#Get token
token = get_api_key("github")
#Get repos
repos = get_repositories(token)
#Print name of repos
for repo in repos:
    print(repo["name"])