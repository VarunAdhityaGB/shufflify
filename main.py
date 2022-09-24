import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

scope = 'playlist-modify-public user-read-playback-state'
username = 'l6pii8uua3baeavix82fbffl7'

token = SpotifyOAuth(scope=scope, username=username, client_id="c1cba650f60b4b69bf66249ba29c1ace", client_secret="fe11c75b2a8a4a56981d7d0d6255d7cf", redirect_uri="http://127.0.0.1:8080")

spotify = spotipy.Spotify(auth_manager=token)

#making a playlist
#name = input("name: ")
#desc = input("descrition: ")
#spotify.user_playlist_create(user=username, public=True, description=desc, name=name)

# adding music to playlist
