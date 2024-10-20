# Spotify Automation Playlist Creation App

A Flask application that automates Spotify playlist creation and management using Spotify’s API and Spotipy library. Authenticate with your Spotify account, view your profile, create playlists, and add songs effortlessly through a web interface.

## Features

- Spotify Authentication: Authenticate securely using OAuth 2.0.
- Profile Management: View your Spotify profile information.
- Playlist Creation: Create new public playlists with ease.
- Add Songs: Add tracks to your playlists using Spotify track URIs.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- Pip (Python package manager)
- Spotify Developer account to create an app and obtain credentials:
  - Client ID
  - Client Secret
  - Redirect URI

## Installation

### Linux

1. Clone the repository

'''bash
git clone <repository-url>
cd <repository-directory>
'''

2. Create a virtual environment

bash'''
python3 -m venv venv
source venv/bin/activate
'''


3. Install the dependencies

'''bash
pip install flask spotipy python-dotenv
'''

4. Configure environment variables

go to .env file add the following details:

CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
REDIRECT_URI=http://your-ec2-instance-ip:8888/callback
SECRET_KEY=your_secret_key

Replace placeholders with your actual Spotify credentials.


5. Run the application

'''bash
python3 app.py
'''

6. Access the app

Open your browser and go to http://<your-ec2-instance-ip>:8888/.



## Windows

1. Clone the repository

'''bash
git clone <repository-url>
cd <repository-directory>
'''

2. Create a virtual environment

'''bash
python -m venv venv
venv\Scripts\activate
'''

3. Install the dependencies

'''bash
pip install flask spotipy python-dotenv
'''

4. Configure environment variables

go to .env file and add the following:

CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
REDIRECT_URI=http://your-ec2-instance-ip:8888/callback
SECRET_KEY=your_secret_key

Replace placeholders with your actual Spotify credentials.


5. Run the application

'''bash
python app.py
'''


6. Access the app

Open your browser and go to http://<your-ec2-instance-ip>:8888/.



## Usage

1. Home Page: Go to the root URL (/) to find the login link.


2. Login: Click on "Login with Spotify" to authenticate.


3. Profile: After authentication, view your profile and options to create playlists or add songs.


4. Create a Playlist: Navigate to /create_playlist to create a new playlist.


5. Add Songs: Use /add_song to add tracks using Spotify track URIs.



## App Endpoints

/: Home page with a link to log in using Spotify.

/login: Redirects users to Spotify for authentication.

/callback: Callback URL for Spotify to redirect after authentication.

/profile: Displays user profile information.

/create_playlist: Creates a new public playlist for the user.

/add_song: A form to add tracks to a playlist using track URIs.


## Environment Variables

CLIENT_ID: Your Spotify app’s client ID.

CLIENT_SECRET: Your Spotify app’s client secret.

REDIRECT_URI: The callback URI registered in your Spotify app.

SECRET_KEY: A secret key for session management in Flask.


## Troubleshooting

If you encounter authentication errors, verify your Spotify credentials in the .env file.

Ensure your Spotify app’s redirect URI matches the one set in the .env file.

Make sure the Flask server is accessible from your Spotify app’s registered redirect URI.


## Contributing

Feel free to fork the repository and submit pull requests for improvements, bug fixes, or new features. Please ensure all contributions are well-documented

### Contact

For any issues or inquiries, please reach out to Rahul yadav.
