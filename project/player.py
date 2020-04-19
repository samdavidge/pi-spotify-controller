from .device import Device
from .spotifyclient import SpotifyClient


class Player:

    def __init__(self, device: Device, spotifyClient: SpotifyClient):
        self.spotifyClient = spotifyClient
        self.device = device

    def play(self):
        self.spotifyClient.makeRequest('me/player/play', 'PUT')

    def pause(self):
        self.spotifyClient.makeRequest('me/player/pause', 'PUT')

    def increaseVolume(self):
        self.setVolume(self.device.increaseVolume())

    def decreaseVolume(self):
        self.setVolume(self.device.decreaseVolume())

    def setVolume(self, volume: int):
        self.spotifyClient.makeRequest('me/player/volume?volume_percent=' + str(volume), 'PUT')

    def nextSong(self):
        self.spotifyClient.makeRequest('me/player/next', 'POST')

    def previousSong(self):
        self.spotifyClient.makeRequest('me/player/previous', 'POST')

    def toggleShuffle(self):
        shuffle = 'true' if self.device.toggleShuffle() else 'false'
        self.spotifyClient.makeRequest('me/player/shuffle?state=' + shuffle, 'PUT')