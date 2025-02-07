from flask import render_template, request, redirect, url_for, session, flash
import routes.singles as singles


def artist(name):
    artist_id = session.get('artist_id')
    results = session.get('artist_results')
    albums = session.get('albums')
    canciones = singles.singles(artist_id)
    user_info = session.get('user_info')

    return render_template('artist_information.html', results = results, albums = albums, singles = canciones, user_info = user_info)