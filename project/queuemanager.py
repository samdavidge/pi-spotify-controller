from .spotifyclient import SpotifyClient
from .player import Player
import random


class QueueManager:

    def __init__(self, spotifyClient: SpotifyClient, player: Player):
        self.spotifyClient = spotifyClient
        self.player = player

    def queueTopTracksForArtist(self, artistId: str):
        tracks = self.spotifyClient.makeRequest('artists/' + artistId + '/top-tracks?country=gb', 'GET')['tracks']
        random.shuffle(tracks)
        first = True
        for track in tracks:
            self.player.queueTrack(track['uri'])
            if first:
                self.player.nextSong()
                first = False
