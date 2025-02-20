from flask import Flask, session, redirect, request, url_for,render_template
from routes import home, search, artist, album_information, callback
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'hadoiehoidaodhafhaklgfaklgfuaeidajkhdakhdeaohdiaed'

@app.route('/')
def index_route():
    token = session.get('token_info')
    user_info = session.get('user_info')
    return render_template('index.html', token = token, user_info = user_info)

@app.route('/home', methods= ['GET','POST'])
def home_route():
    return home.index()

@app.route('/authorize')
def callback_route():
    return callback.callback()


@app.route('/search', methods= ['POST'])
def search_route():
    return search.search()

@app.route('/artist-information/<string:id>', methods=['GET', 'POST'])
def artist_route(id):
    return artist.artist(id)

@app.route('/album-information/<string:id>', methods=['GET', 'POST'])
def alb_information(id):
    return album_information.album_information(id)

@app.route("/logout")
def logout():
    if session:
        session.clear()


    return redirect(url_for('index_route'))

@app.template_filter('format_duration')
def format_duration(value):
    minutes = value // 60000
    seconds = (value // 1000) % 60
    return f"{minutes}:{str(seconds).zfill(2)}"

@app.template_filter('zfill')
def zfill(value, width=2):
    return str(value).zfill(width)

@app.template_filter('datetimeformat')
def datetimeformat(value):
    try:
        date = datetime.strptime(value, '%Y-%m-%d')
        return date.strftime('%B %d, %Y')
    except ValueError:
        try:
            date = datetime.strptime(value, '%Y-%m')
            return date.strftime('%B %Y')
        except ValueError:
            try:
                date = datetime.strptime(value, '%Y')
                return date.strftime('%Y')
            except ValueError:
                return value 

if __name__ == '__main__':
    app.run(debug=True)