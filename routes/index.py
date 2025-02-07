from flask import render_template, request, redirect, url_for, session, flash
from routes import spotify_credentials as spt
def index():
    token_info = session.get('token_info')
    sp = spt.spotipy.Spotify(auth=token_info['access_token'])
    user_info = sp.current_user()

    session['user_info'] = user_info
    
    return render_template('index.html',user_info = user_info)