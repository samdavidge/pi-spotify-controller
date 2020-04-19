from .credentials import Credentials
import json
import os


class CredentialsFactory:
    
    @staticmethod
    def fromFile():
        scriptPath = os.path.dirname(os.path.realpath('__file__'))
        credsPath = os.path.join(scriptPath, '../creds.txt')
        with open('creds.txt') as jsonFile:
           data = json.load(jsonFile)
           creds = Credentials(data['clientId'], data['clientSecret'], data['accessToken'], data['refreshToken'])
           return creds
           