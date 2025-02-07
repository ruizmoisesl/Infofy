from flask import session
from routes.spotify_credentials import sp


def singles(artist_id):
    singles = sp.artist_albums(artist_id, album_type='single', limit=50)
    return singles

