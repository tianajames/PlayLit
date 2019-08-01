# import lib.spotipy
# from lib.spotipy.oauth2 import SpotifyClientCredentials
# import lib.requests
from google.appengine.api import urlfetch
import base64
import urllib
import json

CLIENT_ID = "c7e4559a0c114c7997c575394755f9af"
CLIENT_SECRET = "355dc6a239e1481a85209156a1fcab3b"

def author():
    client_string = '{}:{}'.format(CLIENT_ID, CLIENT_SECRET)
    auth = base64.b64encode(str(client_string)).encode()
    form_fields = {
        "grant_type": "client_credentials"
    }
    form_data = urllib.urlencode(form_fields)
    result = urlfetch.fetch(
        url = "https://accounts.spotify.com/api/token",
        payload = form_data,
        method = urlfetch.POST,
        headers= {
            "Authorization": "Basic " + auth,
        }
    )
    if result.status_code == 200:
        access_token = json.loads(result.content)["access_token"]
        return access_token
    else:
        print result.status_code, result.content
        print "Didnt work"
        return None


urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'


def get_artist():
    headers = {'Authorization': 'Bearer ' + author()}
    result = urlfetch.fetch(
        url = 'https://api.spotify.com/v1/artists/3jOstUTkEu2JkjvRdBA5Gu',
        headers = headers
    )
    return result.content

def get_search(q):
    headers = {'Authorization': 'Bearer ' + author()}
    result = urlfetch.fetch(
        url = 'https://api.spotify.com/v1/search?q=' + q+ '&type=playlist&limit=10',
        headers = headers
    )
    return result.content

def get_tracks(id):
    headers = {'Authorization': 'Bearer ' + author()}
    result = urlfetch.fetch(
        url = 'https://api.spotify.com/v1/playlists/'+id+'/tracks?limit=15',
        headers = headers
    )
    return result.content



# client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID,
#                                                       client_secret=CLIENT_SECRET)
# sp= lib.spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#
# while True:
#     try:
#         artist = sp.artist(urn)
#     except:
#         continue
#     else:
#         print(artist['name'])
#         break
