import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import pandas as pd
from pandas import json_normalize

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

"""
NOTES:
ID & URI columns should never be blank
FutureWarning suppressor imported since .append() for DataFrames was recently deprecated.

"""

def search_artist(artist_name):
    """
    Creating a function that will pull in relevant artist and return a json that will be appended to a pre-existing dataframe for wrangling.

    Input: name of artist as a string
    Output: JSON containing artist's information
    """
    artist_info = sp.search(q=artist_name, type="artist", limit=1)

    return artist_info

def artist(artist_name):
    """
    Creating a function that takes in JSON of artist and returns dictionary/dataframe row containing relevant data.

    Input: searched artist's JSON
    Output: Dataframe row(dictionary) containing relevant information

    Artist Info Needed:
        artist_id
        artist_name
        external_url	
        genre
        image_url
        followers
        popularity
        type
        artist_uri
    """
    musician = search_artist(artist_name)
    
    result = musician['artists']['items'][0]

    artist_id = result['id']
    artist_name = result['name']
    external_url = result['external_urls']['spotify']
    genre = result['genres'][0]
    image_url = result['images'][0]['url']
    followers = result['followers']['total']
    popularity = result['popularity']
    artist_type = result['type']
    artist_uri = result['uri']

    artist_dict = {'artist_id':artist_id, 
                    'artist_name':artist_name, 
                    'external_url':external_url, 
                    'genre':genre, 'image_url':image_url, 
                    'followers': followers,
                    'popularity': popularity, 
                    'type':artist_type, 
                    'artist_uri':artist_uri}
    
    return artist_dict

def search_album(artist_name, country="US"):
    """
    Creating a function that will pull in relevant album based on artist_id and return a json that will be appended to a pre-existing dataframe 
    for wrangling.

    Note: recursively call search_artist's name function to get artist_id to avoid creating multiple for loops later for several artists.
    Making default country US which can be changed at any time.

    Input: artist ID, URI, or URL as a string. For simplicity, will just use artist ID by running search_artist on artist_name
    Output: JSON including album's information
    """

    musician = search_artist(artist_name)
    artist_id = musician['artists']['items'][0]['id']

    album_info = sp.artist_albums(artist_id,country=country, limit=20, offset=0)

    return album_info

def album(artist_name):
    """
    Creating a function that takes in JSON of artist's albums and returns dataframe  containing relevant data.

    Input: album's JSON
    Output: Dataframe containing relevant information

    Album Info Needed:
        album_id
        album_name
        external_url
        image_url
        release_Date
        total_tracks
        type
        album_uri
        artist_id
    """
    album_df = pd.DataFrame()

    artist_albums = search_album(artist_name)['items']

    for album in artist_albums:
        album_dict = {'album_id':album['id'],
                    'album_name':album['name'], 
                    'external_url': album['external_urls']['spotify'],
                    'image_url': album['images'][0]['url'],
                    'release_date': album['release_date'],
                    'total_tracks': album['total_tracks'], 
                    'album_uri': album['uri'], 
                    'artist_id':album['artists'][0]['id']}

        album_df= album_df.append(album_dict, ignore_index = True)
    
    return album_df


def track(artist_name):
    """
    Creating a function that will pull in relevant track based on album_id and return a json that will be appended to a pre-existing dataframe 
    for wrangling.

    Note: recursively call album's name function to get album_id to avoid creating multiple for loops later for several artists.

    Input: List of album ID, URI or URL. Will use album ID for simplicity
    Output: dataframe including track's information

    Track Info Needed:
        track_id
        song_name
        external_url
        duration_ms
        explicit
        disc_number
        type	
        song_uri
        album_id
    """

    artist_albums = album(artist_name)
    album_ids = artist_albums['album_id'].values.tolist()

    track_info = pd.DataFrame()

    for album_id in album_ids:
        track = sp.album_tracks(album_id=album_id, limit=50, offset=0, market=None)
        track_df =  pd.json_normalize(track, record_path=['items'])
        track_df['album_id'] = album_id
        track_info = pd.concat([track_info, track_df])

    track_info = track_info[['id', 'name', 'external_urls.spotify', 'duration_ms', 'explicit', 'disc_number', 'type', 'uri', 'album_id']]

    track_info = track_info.rename(columns = {'id':'track_id',
                                'name':'song_name',
                                'external_urls.spotify': 'external_url',
                                'uri': 'song_uri'
                                })
        
    return track_info

def track_features(artist_name):
    """
    Creating a function that will take in several track ID's from an album and return a DataFrame.

    Note: Double for loop since track_features has a limitation of only taking 100 IDs at a time.

    Input: list of track URIs, URLs or IDs. Using track IDs for simplicity
    Output: DataFram containing the features for each track.

    Track Feature Info Needed:
        track_id
        danceability
        energy
        instrumentaless
        liveness
        loudness
        speechiness
        tempo
        type
        valence
        song_uri
    """
    
    track_df = track(artist_name)
    track_ids = track_df['track_id'].values.tolist()
    
    chunks = [track_ids[x:x+100] for x in range(0, len(track_ids), 100)]

    track_features_df = pd.DataFrame()
    
    for chunk in chunks:
        tracks = sp.audio_features(chunk)
        for track_info in tracks:
            track_feature_dict = {'track_id': track_info['id'], 
                                'danceability': track_info['danceability'],
                                'energy': track_info['energy'],
                                'instrumentalness': track_info['instrumentalness'],
                                'liveness': track_info['liveness'], 
                                'loudness': track_info['loudness'], 
                                'speechiness': track_info['speechiness'], 
                                'tempo': track_info['tempo'],
                                'type': track_info['type'], 
                                'valence': track_info['valence'], 
                                'song_uri': track_info['uri']}
    
            track_features_df = track_features_df.append(track_feature_dict, ignore_index = True)
    
    return track_features_df



