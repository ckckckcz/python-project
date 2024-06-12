import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import sys

def print_lyrics():
    lines = [
        ("please forgive me, i know no what i do", 0.05),
        ("please forgive me, i can't stop loving you", 0.06),
        ("don't deny me, this pain i'm going through", 0.07),
        ("please forgive me, if i need you like i do", 0.05),
        ("please belive me ( Oh belive it ), every word i say is true", 0.08),
        ("please forgive me, i can't stop loving you", 0.06),
    ]

    delays = [0.3, 0.3, 0.4, 0.3, 0.6, 0.07]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(char_delay)
        time.sleep(delays[i])
        print("")

# Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    redirect_uri="YOUR_REDIRECT_URI",
    scope="user-modify-playback-state user-read-playback-state"
))

def play_song(song_uri):
    devices = sp.devices()
    if devices['devices']:
        device_id = devices['devices'][0]['id']
        sp.start_playback(device_id=device_id, uris=[song_uri])
    else:
        print("No active device found")

# Main program
if __name__ == "__main__":
    # Play the song "Please Forgive Me" by Bryan Adams
    song_uri = "spotify:track:6ztstiyZL6FXzh4aG46ZPD"  # URI for "Please Forgive Me"
    play_song(song_uri)

    # Print the lyrics
    print_lyrics()
