from utils import Utils
import urllib.request as request
import re
import youtube_dl
import sys
import time

class Converter():
    sp = None
    SLEEP_TIME = 5
    def __init__(self, username, sp):
        print('Started downloading tracks')
        self.username = username
        self.sp = sp
        self.fetch_tracks_in_playlist()

    def my_hook(self, process):
        if process['status'] == 'finished':
            print('File Downloaded')
        elif process['status'] == 'downloading':
            print('''
                Name: {} \n
                Status: Downloading \n
                Percentant: {} \n
                Eta: {}
            '''.format(process['filename'], process['_percent_str'], process['_eta_str']))

    def fetch_tracks_in_playlist(self):
        playlists = self.sp.user_playlists(self.username)
        for playlist in playlists['items']:
            id = playlist['external_urls']['spotify'].split('/')[4]
            tracks = self.sp.user_playlist_tracks(self.username, id)
            for track in tracks['items']:
                track_name = track['track']['name'].split(' ')
                query = '+'.join(track_name)
                try:
                    youtube_page = request.urlopen('https://youtube.com/results?search_query={}'.format(query))
                except Exception:
                    print('An error occurred during the request.')
                    sys.exit()
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', youtube_page.read().decode())
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'progress_hooks': [self.my_hook],
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    try:
                        ydl.download(['https://www.youtube.com/watch?v={}'.format(str(search_results[0]))])
                        time.sleep(self.SLEEP_TIME) # a constant that stop the execution for 5 seconds, or you will fall in a 503 error. 
                    except Exception:
                        print('A track shouldn\'t be downloaded.')
                        break
        print('\n\n\n\n Tracks Successfully downloaded. Goodbye ;)')
        sys.exit()