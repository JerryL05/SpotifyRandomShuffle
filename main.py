#!/usr/bin/env python3

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import time

# Spotify API credentials
CLIENT_ID = 'c4d325ef9b06444d85ef932b452f53e7'
CLIENT_SECRET = 'b373c273d0a0477fad26465529f7549d'
REDIRECT_URI = 'http://localhost:8888/callback/'

# Spotify scope for playback control, can access private playlists
SCOPE = 'user-modify-playback-state user-read-playback-state playlist-read-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE),
                     requests_timeout=20)  # Increased timeout for slow connections


# Get the active device ID
def get_active_device_id():
    devices = sp.devices()
    for device in devices['devices']:
        if device['is_active']:
            return device['id']
    return None

# Function to fetch all tracks from a playlist
def get_playlist_tracks(playlist_id):
    tracks = []
    results = sp.playlist_items(playlist_id)
    tracks.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return [track['track']['uri'] for track in tracks if track['track']]


# Fisher-Yates shuffle algorithm for a true shuffle with no bias
def true_shuffle(tracks):
    shuffled = tracks.copy()
    for i in range(len(shuffled) - 1, 0, -1):
        j = random.randint(0, i)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    return shuffled

# function to play a shuffled playlist with retries
def play_shuffled_playlist(playlist_id):
    tracks = get_playlist_tracks(playlist_id)
    shuffled_tracks = true_shuffle(tracks)

    device_id = get_active_device_id()
    if not device_id:
        print("No active device found. Please play something on Spotify and try again.")
        return

    # Start playing the first track
    sp.start_playback(device_id=device_id, uris=[shuffled_tracks[0]])

    # Queue tracks with retries
    for track_uri in shuffled_tracks[1:]:
        safe_add_to_queue(track_uri)
        time.sleep(0.3)  # Slight delay to prevent overload

# Retry function for adding to queue
def safe_add_to_queue(track_uri, retries=3):
    for attempt in range(retries):
        try:
            sp.add_to_queue(track_uri)
            print(f"Queued: {track_uri}")
            return
        except Exception as e:
            print(f"Error queuing {track_uri}: {e}")
            time.sleep(2)  # Wait before retrying
    print(f"Failed to queue {track_uri} after {retries} attempts.")

# Function to truncate playlist ID from URL or URI
def sanitize_playlist_id(playlist_id):
    if 'playlist/' in playlist_id:
        return playlist_id.split('playlist/')[1].split('?')[0]
    elif 'spotify:playlist:' in playlist_id:
        return playlist_id.split('spotify:playlist:')[1].split('?')[0]
    elif '?' in playlist_id:
        return playlist_id.split('?')[0]  # Remove all query parameters
    return playlist_id

# Main function to start playback with a shuffled playlist
playlist_id = sanitize_playlist_id('6eIzg2thY40kyyoPxVMu9U?si=4b947c44736c4f53&pt=dbedb742b117835d7f661eb7df00a183')
print(f"Using playlist ID: {playlist_id}")
play_shuffled_playlist(playlist_id)


print("Playback started with a truly shuffled playlist!")
