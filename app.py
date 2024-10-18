from flask import Flask, redirect, request, session, url_for
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import os
import config  # Import the config file

app = Flask(__name__)

# Set your secret key for session management
app.secret_key = config.SECRET_KEY  # Use the secret key from config

# Configure Spotify OAuth
sp_oauth = SpotifyOAuth(
    client_id=config.CLIENT_ID,       # Use the client ID from config
    client_secret=config.CLIENT_SECRET,   # Use the client secret from config
    redirect_uri=config.REDIRECT_URI,  # Use the redirect URI from config
    scope='user-read-private user-read-email playlist-modify-public playlist-modify-private'  # Add scopes for playlist modification
)

@app.route('/')
def index():
    return 'Welcome to the Spotify OAuth app! <a href="/login">Login with Spotify</a>'

@app.route('/login')
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    token_info = sp_oauth.get_access_token(request.args['code'])
    session['token_info'] = token_info
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    if 'token_info' not in session:
        return redirect(url_for('login'))

    token_info = session['token_info']
    sp = Spotify(auth=token_info['access_token'])
    user_info = sp.current_user()

    return f'''
        <h1>Profile</h1>
        <p>Name: {user_info['display_name']}</p>
        <p>Email: {user_info['email']}</p>
        <a href="/create_playlist">Create a Playlist</a><br>
        <a href="/add_song">Add Songs</a>
    '''

@app.route('/create_playlist')
def create_playlist():
    if 'token_info' not in session:
        return redirect(url_for('login'))

    token_info = session['token_info']
    sp = Spotify(auth=token_info['access_token'])

    user_id = sp.current_user()['id']
    playlist_name = 'My New Playlist'
    sp.user_playlist_create(user_id, playlist_name, public=True)

    return f'Playlist "{playlist_name}" created successfully! <a href="/">Go back</a>'

@app.route('/add_song', methods=['GET', 'POST'])
def add_song():
    if request.method == 'POST':
        if 'token_info' not in session:
            return redirect(url_for('login'))

        token_info = session['token_info']
        sp = Spotify(auth=token_info['access_token'])

        playlist_id = '1IuIlTAiGqVAHwe2jODMLf'  # Your Playlist ID
        
        # Get the track URIs from the textarea input
        track_uris = request.form['track_uri'].split(',')  # Split the input string into a list
        track_uris = [uri.strip() for uri in track_uris]  # Clean up any whitespace

        # Add tracks to the playlist
        sp.user_playlist_add_tracks(user=sp.current_user()['id'], playlist_id=playlist_id, tracks=track_uris)

        return f'Songs added to playlist! <a href="/">Go back</a>'

    return '''
        <form method="POST">
            <label for="track_uri">Enter Track URIs (comma-separated):</label><br>
            <textarea name="track_uri" placeholder="spotify:track:URI1,spotify:track:URI2" required></textarea><br>
            <button type="submit">Add Songs</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

