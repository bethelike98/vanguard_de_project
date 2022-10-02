# README

## Overview
Ingested data from Spotify (artist info, album info, track info, track_feature info) using Spotipy API for 20 of my favorite artists, cleaned up the JSON formatted data into Dataframe, and loaded into a SQLite database.

### Step 1: Extracting and Transforming
Contained within submissions/Ingestion_Extraction_Code folder. <br />
functions.py is a helper functions file that pulls the data in from Spotify in JSON format and wrangles the data for DataFrame format.
extract_transform.py further wrangles the DataFrame data by dropping null values and duplicate values, where appropriate.

### Step 2: Loading/Analytics
Contained within submissions/SQLite_Code.py folder. <br />
table_creation_queries.py and view_creation_queries.py are multi-line comments within a Python file that I used to write out queries to create tables and views for data I needed uploaded to my database (spotify.db file in same folder). <br />
db_creation.py is the Python file that I use to create the database, connect to the database, create tables and views referenced in table_creation_queries.py and view_creation_queries.py file. Final step was uploading dataframes from step 1 into newly defined tables. <br />
Views Contained: <br />

* Top 10 songs by artist in terms of duration_ms (ordered by artist ASC, duration_ms DESC)
* Top 20 artists in the database ordered by # of followers DESC
* Top 10 songs by artist in terms of tempo (ordered by artist ASC, tempo DESC)
* Top 5 most energetic artists
* Each artist's first released album

### Step 3: Visualization
Contained within submissions/Visualization_Code folder.
correlation_matrix_viz.py shows a correlation matrix/heatmap using track feature's danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, valence metrics.
danceability_per_artist_viz.py shows violin charts of danceability per artist. A violin plot depicts distributions of numeric data for one or more groups using density curves.
longest_song_viz.py shows bar charts of the top 5 longest songs (in ms) per artist and the name of each song.

Spotify Database ERD
<img width="1361" alt="Spotify Database ERD" src="https://user-images.githubusercontent.com/87020742/193469214-1966dc3c-c08b-4401-bbef-7a1484be55b1.png">

├── vanguard_de_project
│   ├── submissions
│   │   ├── Ingestion_Extraction_Code
│   │   |   ├── extract_transform.py
│   │   |   ├── functions.py
│   │   ├── SQLite_Code
│   │   |   ├── db_creation.py
│   │   |   ├── spotify.db
│   │   |   ├── table_creation_queries.py
│   │   |   ├── view_creation_queries.py
│   │   ├── Visualization_Code
│   │   |   ├── correlation_matrix_viz.py
│   │   |   ├── danceability_per_artist_viz.py
│   │   |   ├── longest_song_viz.py
│   │   ├── .DS_Store
│   │   ├── Ingestion_Extraction_Code
│   |   ├── views
│   |   ├── Visualizations.pdf
│   |   ├── readme.md
│   ├── .DS_Store
│   ├── .gitignore
│   ├── README.md
│   ├── spotipy_sample.py
