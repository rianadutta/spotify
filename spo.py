import pandas as pd
import tekore as tk
import spotipy


#using a content based recommender system

#references: https://towardsdatascience.com/recommendation-systems-explained-a42fc60591ed


from spotipy.oauth2 import SpotifyClientCredentials


cid = '433d102e6001489097941adc2fbdd356'
secret = '6aab6d08461c41cdb77117620993419d'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
#sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

app_token = tk.request_client_token(cid,secret)
spotify = tk.Spotify(app_token)

# part 1: prompt user to type in a track name/artist and rank it out of 10
#TODO error handling if user doesn't behave as expected

songs = []
ranks = []
number = input("How many songs would you like to input? ")
for n in range(int(number)):
    search = input("Search for a song (specify artist name to be specific): ")
    s1, = spotify.search(search, ('track',), None, None)
    print(s1.items[0].name + " by", end = ' ')
    for artist in s1.items[0].artists:
        print(artist.name, end=" ")
    print(" ")
    rank = int(input("Rank this song from 1-10: "))
    songs.append(s1.items[0])
    ranks.append(rank)

if len(songs) != len(ranks):
    assert False 



name = []
acousticness = []
danceability = []
energy = []
instrumentalness = []
key = []
liveness = []
loudness = []
time_signature = []
#album = spotify.album('6AORtDjduMM3bupSWzbTSG')
#for track in album.tracks.items:
 #   id = track.id
    
  #  name.append(spotify.track(id).name)
   # acousticness.append(spotify.track_audio_features(id).acousticness)
    #danceability.append(spotify.track_audio_features(id).danceability)
    #energy.append(spotify.track_audio_features(id).energy)
    #instrumentalness.append(spotify.track_audio_features(id).instrumentalness)    

  #  key.append(spotify.track_audio_features(id).key)
   # liveness.append(spotify.track_audio_features(id).liveness)
  #  loudness.append(spotify.track_audio_features(id).loudness)
  #  time_signature.append(spotify.track_audio_features(id).time_signature)

#data = [name, acousticness, danceability,energy,instrumentalness,key,liveness,loudness,time_signature]

#df = {"Name":name, "Acousticness":acousticness,"Danceability":danceability, "Energy":energy,"Instrumentalness":instrumentalness,"Key":key,"Liveness":liveness,"Loudness":loudness,"Time Signature":time_signature}
#print(pd.DataFrame(df))


# TO DO: ui to ask for songs and get them into a list based on track id and ranking out of 10
# for now will be using evermore album tracks

#track_id = sp.search(q='artist: ' + "taylor swift" + 'track:' + "love", type='track')
#print(track_id)