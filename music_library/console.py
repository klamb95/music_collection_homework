import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist('Twenty One Pilots')
artist_2 = Artist('Biffy Clyro')

album_1 = Album('Trench', 'Twenty One Pilots')
album_2 = Album('Only Revolutions', 'Biffy Clyro')

album_repository.save(album_1)
album_repository.save(album_2)



pdb.set_trace()
