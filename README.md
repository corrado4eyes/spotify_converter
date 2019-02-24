# Spotify Converter

Have you ever desired to download your whole library from spotify? I did.

# Installation
---
`pip install -r requirements.txt`

# Usage
---
* 1: Create your own application on [spotify](https://developer.spotify.com/)
* 2: Exports the CLIENT_ID and the CLIENT_SECRET using on terminal:
    ```
        export CLIENT_ID='your_client_id'
        export CLIENT_SECRET='your_client_secret'
    ```
* 3: Register a REDIRECT_URI on your application's settings. If you use a different endpoint like `https://somewhere.somedomain/someendpoint` don't forget to change on spotify_auth.py file the endpoint of flask.
* 4: `python3 __main__.py *your_username*`
* 5: Enjoy your tracks
