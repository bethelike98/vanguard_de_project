sql_create_artists_table = """
        CREATE TABLE IF NOT EXISTS artist (
            artist_id   varchar(50)     PRIMARY KEY,
            artist_name     varchar(255)    NOT NULL,
            external_url    varchar(100)    NOT NULL UNIQUE,
            genre   varchar(100),
            image_url   varchar(100),
            followers   integer,
            popularity  integer,
            type    varchar(50),
            artist_uri  varchar(100)    NOT NULL UNIQUE
        );
 """


sql_create_album_table = """
        CREATE TABLE IF NOT EXISTS album(
            album_id    varchar(50) PRIMARY KEY,
            album_name  varchar(255) NOT NULL,
            external_url    varchar(100)    NOT NULL UNIQUE,
            image_url   varchar(100),
            release_date    text,
            total_tracks    integer,
            type    varchar(50),
            album_uri   varchar(100)    NOT NULL UNIQUE,
            FOREIGN KEY (artist_id) REFERENCES artist (artist_id)
        );
"""


sql_create_track_table = """
        CREATE TABLE IF NOT EXISTS track(
            track_id    varchar(50) PRIMARY KEY,
            song_name   varchar(255)    NOT NULL,
            external_url    varchar(100)    NOT NULL UNIQUE,
            duration_ms     integer,
            explicit    boolean,
            disc_number integer,
            type    varchar(50),
            song_uri    varchar(100)    NOT NULL UNIQUE,
            FOREIGN KEY (album_id)  REFERENCES  album (album_id)           
        );
"""


sql_create_track_feature_table = """
        CREATE TABLE IF NOT EXISTS track_feature(
            danceability    double,
            energy  double,
            instrumentalness    double,
            liveness    double,
            speechiness double,
            tempo   double,
            type    varchar(50),
            valence double,
            FOREIGN KEY (song_uri)  REFERENCES track (song_uri),
            FOREIGN KEY (track_id) REFERENCES track (track_id)
        );
"""