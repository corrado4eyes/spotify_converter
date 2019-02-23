from utils import Utils
import spotipy.util as sp_utils
from flask import Flask,request,abort,jsonify, Response, json
from spotipy.oauth2 import SpotifyClientCredentials


app = Flask(__name__)

utils = Utils()

@app.route('/', methods = ['GET'])
def fetch_permissions_request():
    client_credentials_manager = SpotifyClientCredentials(utils.CLIENT_ID, utils.CLIENT_SECRET)
    return client_credentials_manager   