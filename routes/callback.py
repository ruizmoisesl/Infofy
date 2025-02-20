from flask import render_template, request, redirect, url_for, session, flash
import routes.spotify_credentials as spotify_credentials

def callback():
    code = request.args.get('code')
    token_info = spotify_credentials.sp_oauth.get_access_token(code)
    session['token_info'] = token_info
    return redirect(url_for('home_route'))