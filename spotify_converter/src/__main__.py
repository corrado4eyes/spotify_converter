from converter import Converter
import sys
from spotify_auth import fetch_permissions_request
import spotipy
username = ''

playlists = {}

if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("You have also to insert your username.")
        sys.exit()

    client_credentials = fetch_permissions_request()

    sp = spotipy.Spotify(client_credentials.get_access_token())
    converter = Converter(username, sp)
    converter.fetch_tracks_in_playlist()

    