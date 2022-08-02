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

ids = getTrackIDs('Romir Varshney', '0IzD6mie2jVgjMO139wPMZ') # Take the Top Off
#ids = getTrackIDs('Romir Varshney', '5ZIFa3koaqbNG7WBqSpcdg') # Curry Muncher

avgDance = 0.00000000
keyArray = [] * len(ids)


def getTrackFeatures(id):
  global avgDance
  meta = sp.track(id)
  features = sp.audio_features(id)
  

  # print((sp.audio_features(id)[0]['key'])) # line that gives the line including the key
  

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

  key = sp.audio_features(id)[0]['key']
  keyArray.append(key)


  track = [name, album, artist, release_date, length, popularity, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
  return track

 
print("There are " + str(len(ids)) + " songs in this playlist")
#print(ids)


tracks = []
for i in range(len(ids)):

  track = getTrackFeatures(ids[i])
  tracks.append(track)
  print(tracks[i])

albums = [row[1] for row in tracks]
# print(albums)

tempos = [row[14] for row in tracks]
# print(tempos)

names = [row[0] for row in tracks]

nameSet = []
tierOne = []
tierTwo = []
keySet = []
tierThree = set()


print()
print("These are all the songs in the playlist.")
print(names)

#q = 0
#while(q < 1):
  #x = input("Enter the name of the song that you want to use: ")
  #if x in names:
    #q = 3
    #print(x, "was found in the playlist")
    #index = names.index(x)
    #print("The index of the name is ", index)

#z = tempos[index]
#print("The BPM is ", z)

diff = 999
diffIndex = 0

for j in range(len(ids)):
  x = tempos[j]
  for i in range(len(ids)):

    if (i == j):
      continue

    z = tempos[i]
    if(abs(x - z) <= 3.1):
      if(names[i] == names[j]):
        continue
      else:
        nameSet.append(names[i])
        nameSet.append(names[j])
        keySet.append(keyArray[i])
        keySet.append(keyArray[j])


        #print("Based on BPM, the best mashup pair in the playlist would be")
        #print()
        #print(names[j], "X", names[i])
        #print()
#print(nameSet)


for i in range(len(names) - 1):
  x = keySet[i]
  a = nameSet[i]
  i = i + 1
  z = keySet[i]
  b = nameSet[i]

  if((abs(x - z) <= 0.1) and (a != b)): # and include BPM in the conditional
        tierOne.append(a)
        tierOne.append(b)
        #print("Based on key, a tier 1 pair in the playlist would be")
        #print()
        #print(a, "X", b)
        #print()
  elif(((abs(x - z) == 5) or abs((x + 12) - z == 5) or abs(x - (z + 12)) == 5) and (a != b)):
    tierTwo.append(a)
    tierTwo.append(b)
    #print("Based on key, a tier 2 pair in the playlist would be")
    #print()
    #print(a, "X", b)
    #print()

getTrackFeatures(ids[i])

print("Tier One", tierOne)
#print("Tier Two", tierTwo)
print()

print("Tier One Pairs (Similar BPM and Same Key)")
print()
for i in range(0, len(tierOne), 4):
  a = tierOne[i]
  i = i + 1
  b = tierOne[i]
  print(a, "-", b)

print()
print("Tier Two Pairs (Similar BPM and Harmonic Fifth Key)")
print()
for i in range(0, len(tierTwo), 4):
  a = tierTwo[i]
  i = i + 1
  b = tierTwo[i]
  print(a, "-", b)

print("Ending Program...")
