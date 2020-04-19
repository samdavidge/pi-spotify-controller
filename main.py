from project.credentialsfactory import CredentialsFactory
from project.spotifyclient import SpotifyClient
from project.player import Player
from project.queuemanager import QueueManager
from evdev import InputDevice, categorize, ecodes
import urllib

spotifyClient = SpotifyClient(CredentialsFactory.fromFile())

device = spotifyClient.getCurrentDevice()

if device:
    player = Player(device, spotifyClient)
    queueManager = QueueManager(spotifyClient, player)

gamepad = InputDevice('/dev/input/event2')

buttons = {
    'aBtn': 289,
    'bBtn': 290,
    'xBtn': 288,
    'yBtn': 291,
    'lBtn': 292,
    'rBtn': 293,
    'selBtn': 296,
    'staBtn': 297,
    'leftUpPad': 0,
    'rightDownPad': 255,
    'centerPad': 127
}

# Handle input
for event in gamepad.read_loop():
    # Buttons
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == buttons['xBtn']:
                print("X")
            elif event.code == buttons['bBtn']:
                print("B")
            elif event.code == buttons['aBtn']:
                queueManager.queueTopTracksForArtist('50nN8IFD4xA67fI4jYbLV4')  # Kano
            elif event.code == buttons['yBtn']:
                print("Y")
            elif event.code == buttons['lBtn']:
                player.previousSong()
            elif event.code == buttons['rBtn']:
                player.nextSong()
            elif event.code == buttons['selBtn']:
                try:
                    player.toggleShuffle()
                except urllib.error.HTTPError:
                    print('You cannot use shuffle in this context')
            elif event.code == buttons['staBtn']:
                try:
                    player.pause()
                except urllib.error.HTTPError:
                    player.play()

    # Analog gamepad
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        # Left, Right and Center
        if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
            if absevent.event.value == buttons['leftUpPad']:
                print("Left")
            elif absevent.event.value == buttons['rightDownPad']:
                print("Right")
            elif absevent.event.value == buttons['centerPad']:
                print("Center")
        # Up, Down and Center
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
            if absevent.event.value == buttons['leftUpPad']:
                player.increaseVolume()
            elif absevent.event.value == buttons['rightDownPad']:
                player.decreaseVolume()
            elif absevent.event.value == buttons['centerPad']:
                print("Center")