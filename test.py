import spotipy
import spotipy.util as util
import random

CLIENT_ID = "c7e4559a0c114c7997c575394755f9af"
CLIENT_SECRET = "355dc6a239e1481a85209156a1fcab3b"
token = util.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

cache_token = token.get_access_token()
spotify = spotipy.Spotify(cache_token)

# replace with predefined buttons
mood = raw_input("Type in a mood: ")
# searches for 5 playlists with mood
search_playlist = spotify.search(mood,limit=5, offset=0, type='playlist')
# selects a random playlist out of the 5 options
search_playlist = random.choice(search_playlist['playlists']['items'])
# prints the name
print(search_playlist['name'])
# use playlist name to find all songs in playlist
# add desired songs to playlist



#results1 = spotify.user_playlists('batldre', limit=1, offset=0)
#print(results1['items'][0]['name'])

# playlists = spotify.user_playlists('batldre')
#
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = spotify.next(playlists)
#     else:
#         playlists = None
