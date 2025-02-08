import spotipy
from spotipy.oauth2 import SpotifyClientCredentials,SpotifyOAuth

client_id= 'a4ef06c5cd894da8af06ecd1c77ad004'
secret_client= 'b1ae99e13ba54f9c8b01063bce8c6aef'
SPOTIPY_REDIRECT_URI = 'https://infofy.vercel.app/authorize'

client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = secret_client)
sp = spotipy.Spotify(client_credentials_manager= client_credentials_manager)

sp_oauth = SpotifyOAuth(client_id=client_id,
                        client_secret=secret_client,
                        redirect_uri=SPOTIPY_REDIRECT_URI,
                        scope='user-library-read')
