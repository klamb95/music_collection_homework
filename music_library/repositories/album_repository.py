from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository

def save(album):
    # sql = "INSERT INTO albums (title, genre, artist_name) VALUES (%s, %s, %s) RETURNING *"
    # values = [album.title, album.genre, album.artist_name]
    # results = run_sql(sql, values)
    # id = results[0]['id']
    # album.id = id
    # return album
    pass

    

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)
    
        


def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        album = Album(result['title'], result['genre'], result['artist_name'], result['id'])
        return album
    



def delete(id):
    sql = "DELETE FROM albums WHERE id= %s"
    values = [id]
    run_sql(sql, values)
    







    # albums = []

    # for row in results:
    #     album = Album(row['title'], row['artist_name'], row['id'])
    #     albums.append(album)
    # return albums