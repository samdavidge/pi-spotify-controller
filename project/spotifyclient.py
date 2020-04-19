import urllib.request
import urllib.parse
import urllib.response
import json
import time
from .credentials import Credentials
from .device import Device


class SpotifyClient:

    def __init__(self, credentials: Credentials):
        self.credentials = credentials
        self.url = 'https://api.spotify.com/v1/'
        self.refreshTokenIfExpired()

    def makeRequest(self, path: str, method: str):
        headers = {'Authorization': 'Bearer ' + self.credentials.accessToken}
        req = urllib.request.Request(self.url + path, headers=headers, method=method)
        with urllib.request.urlopen(req) as response:
            body = response.read().decode("utf-8")
            return json.loads(body) if body else ''

    def getCurrentDevice(self):
        data = self.makeRequest('me/player', 'GET')
        if(data):
            id = data['device']['id']
            active = data['device']['is_active']
            name = data['device']['name']
            volume = data['device']['volume_percent']
            shuffle = data['shuffle_state']
            device = Device(id, active, name, volume, shuffle)
        else:
            device = False
        return device

    def refreshTokenIfExpired(self):
        now = time.time()
        if(now >= self.credentials.expires):
            values = {'grant_type': 'refresh_token',
                      'refresh_token': self.credentials.refreshToken,
                      'client_id': self.credentials.clientId,
                      'client_secret': self.credentials.clientSecret}
            data = urllib.parse.urlencode(values)
            data = data.encode('ascii')
            req = urllib.request.Request('https://accounts.spotify.com/api/token', data=data, method='POST')
            with urllib.request.urlopen(req) as response:
                body = response.read().decode("utf-8")
                body = json.loads(body)
                self.credentials.updateAccessToken(body['access_token'], now, body['expires_in'])