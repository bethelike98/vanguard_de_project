import sqlite3
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

def create_dataframe(db, query):
    con = sqlite3.connect(db)
    df = pd.read_sql_query(query, con)

    return df

### Going to do a correlation matrix between track feature metrics.
 
corr_metrics = """
    SELECT 
        danceability,
        energy, 
        instrumentalness,
        liveness,
        loudness,
        speechiness,
        tempo,
        valence
    FROM track_feature;
"""

db = "spotify.db"

corr_metrics_df = create_dataframe(db, corr_metrics)

corrmatrix = corr_metrics_df.corr()
sns.heatmap(corrmatrix, annot =True)
plt.title('Correlation Matrix for Track Features')
plt.tight_layout()
plt.savefig('Correlation Matrix Track Features.png')
