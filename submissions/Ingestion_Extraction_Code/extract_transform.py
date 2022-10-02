from functions import *

"""
EXTRACTION:

Creating a list of 20 artists to pull in data for.

Will create 4 dataframes to store data for all artists in different tables.

Removing deluxe from albums in case of duplicates.
"""

artists = ['Shawn Mendes', 'Shakira', 'Drake', 'The 1975', 'Majid Jordan',
            'Khalid', 'Beyonce', 'Justin Bieber', 'Mahalia', 'Paramore',
            'Burna Boy', 'Twenty One Pilots', 'Doja Cat', 'The Nieghborhood', 'Coldplay',
            'Rihanna', 'Sam Smith', '6LACK', 'Alina Baraz', 'Fifth Harmony']


artist_df = pd.DataFrame()
album_df = pd.DataFrame()
track_df = pd.DataFrame()
track_features_df = pd.DataFrame()


for artist_name in artists:
    artist_info = artist(artist_name)
    artist_df = artist_df.append(artist_info, ignore_index = True)

    album_info = album(artist_name)
    album_info['album_name'] = album_info['album_name'].str.lower().str.replace(' (deluxe)', '')
    album_info = album_info.drop_duplicates(subset=['album_name']) 
    album_df = album_df.append(album_info, ignore_index = True)
    
    track_info = track(artist_name)
    track_info = track_info.drop_duplicates(subset='song_name')
    track_df = track_df.append(track_info, ignore_index = True)

    track_features_info = track_features(artist_name)
    track_features_df = track_features_df.append(track_features_info, ignore_index = True)


"""
TRANSFORMATION:

Checking that all ID, URI, & URL columns are not null
Already deduped album names by artist within album table - Spotify issue where duplicate albums can exist for same album
Already deduped track names by artist within track table - artist could have same song as single and within album
"""

#################################################### ARTIST TABLE ####################################################

# Dropping any instances of null values across ID, URI, & URL columns
artist_df = artist_df.dropna(subset=['artist_id', 'external_url', 'artist_uri'])

# Dropping any instances of duplicates across ID, URI, & URL columns
artist_df = artist_df.drop_duplicates(subset=['artist_id', 'external_url', 'artist_uri'])


#################################################### ALBUM TABLE ####################################################

# Dropping any instances of null values across name, album_ID, artist_ID, URI, & URL columns
album_df = album_df.dropna(subset=['artist_id', 'external_url', 'album_uri', 'album_id', 'album_name'])

# Dropping any instances of duplicates across  ID, URI, & URL columns
album_df = album_df.drop_duplicates(subset=['external_url', 'album_uri', 'album_id'])


#################################################### TRACK TABLE ####################################################

# Dropping any instances of null values across name, album_ID, track_id, URI, & URL columns
track_df = track_df.dropna(subset=['track_id', 'external_url', 'song_name', 'song_uri', 'album_id'])

# Dropping any instances of duplicates across  ID, URI, & URL columns
track_df = track_df.drop_duplicates(subset=['external_url', 'track_id', 'song_uri'])


#################################################### TRACK FEATURE TABLE ####################################################

# Dropping any instances of null values across track_id & song_uri columns.
track_features_df = track_features_df.dropna(subset=['track_id','song_uri'])

# Dropping any instances of duplicates across  ID, URI columns
track_features_df = track_features_df.drop_duplicates(subset=[ 'track_id', 'song_uri'])

