from flask import  request, redirect, url_for, session, flash
from routes.spotify_credentials import sp

def search():
    if session:
        session.pop('artist_results', None)
        session.pop('albums', None)


    if request.method == 'POST':
        nombre_artista = request.form['artist']

        results = sp.search(q=str(nombre_artista), type= 'artist', limit=1)
        artist_id = results['artists']['items'][0]['id']
        id = results['artists']['items'][0]['id']

        albums = sp.artist_albums(artist_id, album_type='album')
        singles = sp.artist_albums(artist_id, album_type='single', limit= 10)
        
        session['artist_id']= artist_id
        session['artist_results'] = results
        session['albums'] = albums

        return redirect(url_for('artist_route', id = id))
