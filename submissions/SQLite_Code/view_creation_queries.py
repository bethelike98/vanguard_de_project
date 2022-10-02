view_top_10_duration = """
CREATE VIEW top_10_duration_view
AS
SELECT 
    artist_name, 
    SUM(duration_ms) AS duration_ms
FROM artist
JOIN album
ON artist.artist_id = album.artist_id
JOIN track
ON album.album_id = track.album_id
GROUP BY 1
ORDER BY artist_name ASC, duration_ms DESC 
LIMIT 10; """

view_top_20_followers = """
CREATE VIEW top_20_followers_view
AS
SELECT
    artist_name, 
    followers
FROM artist
ORDER BY followers DESC
LIMIT 20;
"""

view_top_10_tempo = """
CREATE VIEW top_10_tempo_view
AS
SELECT 
    artist_name, 
    AVG(tempo) as average_tempo
FROM artist
JOIN album
ON artist.artist_id = album.artist_id
JOIN track
ON album.album_id = track.album_id
JOIN track_feature
ON track.track_id = track_feature.track_id
GROUP BY 1
ORDER BY artist_name, average_tempo DESC
LIMIT 10;
"""

view_top_5_energetic_artists= """
CREATE VIEW top_5_energetic_artists_view
AS
SELECT 
    artist_name,
    AVG(energy) as average_energy
FROM artist
JOIN album
ON artist.artist_id = album.artist_id
JOIN track
ON album.album_id = track.album_id
JOIN track_feature
ON track.track_id = track_feature.track_id
GROUP BY 1
ORDER BY artist_name, average_energy DESC
LIMIT 5;
"""

view_earliest_artist_album = """
CREATE VIEW earliest_artist_album_view
AS
SELECT 
    artist_name,
    album_name
FROM artist
JOIN album 
ON artist.artist_id = album.artist_id
HAVING MIN(release_date);
"""

