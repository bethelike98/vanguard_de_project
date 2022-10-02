import sqlite3
from sqlite3 import Error
from Ingestion_Extraction_Code.extract_transform import *
from table_creation_queries import *
from view_creation_queries import *

def create_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table_view(conn, create_table_sql):
    """ create a table or view from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_df(conn, df, name):
    """
    Insert dataframe into created tables
    :param conn:
    :param df:
    :param name:
    :return: 
    """

    df.to_sql(name, con=conn, if_exists='replace',index=False)

def main():
    database_name = "spotify.db"

    conn = create_connection(database_name)

    ### Table Creation
    create_table_view(conn, sql_create_artists_table)
    create_table_view(conn, sql_create_album_table)
    create_table_view(conn, sql_create_track_table)
    create_table_view(conn, sql_create_track_feature_table)

    insert_df(conn, artist_df, 'artist')
    insert_df(conn, album_df, 'album')
    insert_df(conn, track_df, 'track')
    insert_df(conn, track_features_df, 'track_feature')

    ### View Creation
    create_table_view(conn, view_top_10_duration)
    create_table_view(conn, view_top_20_followers)
    create_table_view(conn, view_top_10_tempo)
    create_table_view(conn, view_top_5_energetic_artists)
    create_table_view(conn, view_earliest_artist_album)


    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()