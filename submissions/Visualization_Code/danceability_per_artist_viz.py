import sqlite3
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

def create_dataframe(db, query):
    con = sqlite3.connect(db)
    df = pd.read_sql_query(query, con)

    return df

### Graphing longest songs by artists
track_per_artist= """
SELECT
    artist_name,
    danceability
FROM artist
JOIN album
ON artist.artist_id = album.artist_id
JOIN track
ON album.album_id = track.album_id
JOIN track_feature
ON track.track_id = track_feature.track_id
"""

db = "spotify.db"

track_per_artist_df = create_dataframe(db, track_per_artist)

sns.set(style="dark")

ax = sns.violinplot(x="artist_name", y="danceability", data=track_per_artist_df)

plt.xticks(rotation = 90)
plt.title('Danceability by Artist')
plt.tight_layout()
plt.savefig('Danceability by Artist.png')