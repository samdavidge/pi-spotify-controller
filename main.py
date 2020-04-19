from project.credentials import Credentials
from project.spotifyclient import SpotifyClient
from project.player import Player

clientId = ''
clientSecret = ''
accessToken = ''
refreshToken = ''

creds = Credentials(clientId, clientSecret, accessToken, refreshToken)
spotifyClient = SpotifyClient(creds)

device = spotifyClient.getCurrentDevice()

if device:
    player = Player(device, spotifyClient)
    player.play()
else:
    print('Nope')