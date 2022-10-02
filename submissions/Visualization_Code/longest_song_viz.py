import sqlite3
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

def create_dataframe(db, query):
    con = sqlite3.connect(db)
    df = pd.read_sql_query(query, con)

    return df

### Graphing longest songs by artists
artist_longest_song = """
SELECT
    artist_name,
    song_name,
    MAX(duration_ms) AS duration_ms
FROM artist
JOIN album
ON artist.artist_id = album.artist_id
JOIN track
ON album.album_id = track.album_id
GROUP BY 1,2
ORDER BY duration_ms DESC
LIMIT 6"""

db = "spotify.db"

artist_longest_song_df = create_dataframe(db, artist_longest_song)

artist_name = artist_longest_song_df['artist_name'].values.tolist()[1:6]
duration = artist_longest_song_df['duration_ms'].values.tolist()[1:6]

song_name = artist_longest_song_df['song_name'].values.tolist()[1:6]
print(song_name)

ax = sns.barplot(x='artist_name', y='duration_ms', data = artist_longest_song_df)
for i, (name, duration) in enumerate(zip(artist_name, duration)):
    ax.text(i, duration-250000, song_name[i], color='black',
            ha='center', va='center', wrap = True, rotation=-90, fontsize=8)
ax.set_ylabel('duration_ms')
ax.set_title('Top 5 Longest Song By Artist')
plt.xticks(label=artist_name) # remove the xticks, as the labels are now inside the bars

plt.savefig('Top 5 Longest Song By Artist.png')
