
import json
import requests
from secrets import spotify_user_id, spotify_token
import spotipy
from spotipy import Spotify as sp
from spotipy.oauth2 import SpotifyClientCredentials
import os
import sys
import time
import json
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError



#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id = "519d971201994261b73be900b361d71b", client_secret = "81a8f4609e7a46369b91c35779ebe986")
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def getTrackIDs(user, playlist_id):
    ids = []
    
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

#ids = getTrackIDs('angelicadietzel', '4R0BZVh27NUJhHGLNitU08')
ids = getTrackIDs('Romir Varshney', '5ZIFa3koaqbNG7WBqSpcdg')

avgDance = 0.00000000

def getTrackFeatures(id):
  global avgDance
  meta = sp.track(id)
  features = sp.audio_features(id)

  # meta
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  release_date = meta['album']['release_date']
  length = meta['duration_ms']
  popularity = meta['popularity']

  # features
  acousticness = features[0]['acousticness']
  danceability = features[0]['danceability']
  energy = features[0]['energy']
  instrumentalness = features[0]['instrumentalness']
  liveness = features[0]['liveness']
  loudness = features[0]['loudness']
  speechiness = features[0]['speechiness']
  tempo = features[0]['tempo']
  time_signature = features[0]['time_signature']

  # custom arrays

  nameArray = [] * len(ids)
  tempoArray = [] * len(ids)



  track = [name, album, artist, release_date, length, popularity, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
  return track

 
print("There are " + str(len(ids)) + " songs in this playlist")
#print(ids)

tracks = []
for i in range(len(ids)):
  #time.sleep(.5)
  #print("Song Name: ", track['name'])

  track = getTrackFeatures(ids[i])
  tracks.append(track)
  print(tracks[i])

print("Individual Features")

albums = [row[1] for row in tracks]
print(albums)

tempos = [row[14] for row in tracks]
print(tempos)



getTrackFeatures(ids[i])
print("Ending Program...")
