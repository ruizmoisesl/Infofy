from flask import  request, render_template,redirect, url_for, session, flash
from routes.spotify_credentials import sp

def album_information(id):
    album = sp.album(id)
    album_tracks = sp.album_tracks(id)
    user_info = session.get('user_info')

    return render_template('album_details.html', album_tracks=album_tracks, album = album, user_info = user_info)