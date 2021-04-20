from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums(title, artist_name) VALUES (%s, %s) RETURNING *"
    values = [album.title, album.artist_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

    

def delete_all():
    pass


def select(id):
    pass


def delete(id):
    pass
