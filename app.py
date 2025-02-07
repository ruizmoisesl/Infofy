from flask import Flask, session, redirect, request, url_for
from routes import index, search, artist, album_information, spotify_credentials
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secretkeyas'

@app.route('/', methods= ['GET','POST'])
def index_route():
    token_info = session.get('token_info', None)
    if not token_info:
        auth_url = spotify_credentials.sp_oauth.get_authorize_url()
        return redirect(auth_url)
    return index.index()

@app.route('/authorize')
def callback():
    code = request.args.get('code')
    token_info = spotify_credentials.sp_oauth.get_access_token(code)
    session['token_info'] = token_info
    return redirect(url_for('index_route'))


@app.route('/search', methods= ['POST'])
def search_route():
    return search.search()

@app.route('/artist-information/<string:id>', methods=['GET', 'POST'])
def artist_route(id):
    return artist.artist(id)

@app.route('/album-information/<string:id>', methods=['GET', 'POST'])
def alb_information(id):
    return album_information.album_information(id)

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