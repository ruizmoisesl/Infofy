from flask import render_template, request, redirect, url_for, session, flash
from routes import spotify_credentials as spt
def index():

    if session:
        token_info = session.get('token_info', None)
        
        sp = spt.spotipy.Spotify(auth=token_info['access_token'])
        user_info = sp.current_user()

        session['user_info'] = user_info
    

    else:
        return redirect(url_for('index_route'))

    return render_template('home.html',user_info = user_info)