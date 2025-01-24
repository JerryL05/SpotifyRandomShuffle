# Spotify True Shuffle

Spotify True Shuffle is a Python project that provides a more authentic random shuffle feature for Spotify playlists. Using Spotify's Web API, this script fetches tracks from a playlist, applies a Fisher-Yates shuffle for true randomness, and plays the tracks in the shuffled order.

## Features
- Fetch all tracks from a specified Spotify playlist.
- Shuffle tracks using a true random algorithm.
- Queue tracks in shuffled order for playback.

## Requirements

### Spotify Developer Account
To use this script, you need to register for a Spotify Developer Account and create an application to get your **Client ID** and **Client Secret**.

### Python Dependencies
- Python 3.7+
- `spotipy`
- `python-dotenv` (optional, for managing credentials)

Install dependencies using pip:
```bash
pip install spotipy python-dotenv
```

## Setup

### Step 1: Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/JerryL05/SpotifyTrueShuffle.git
cd SpotifyTrueShuffle
```

### Step 2: Configure Spotify API Credentials
1. Log in to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Create a new application and retrieve your **Client ID** and **Client Secret**.
3. Add the following redirect URI in the app settings:
   ```
   http://localhost:8888/callback/
   ```

### Step 3: Set Environment Variables
Create a `.env` file in the project root:
```bash
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
REDIRECT_URI=http://localhost:8888/callback/
```

### Step 4: Run the Script
Run the script to shuffle and play a playlist:
```bash
python main.py
```
When prompted, authenticate with your Spotify account.

## Usage

### Run the Script
Specify the playlist ID or URL to shuffle:
```bash
python main.py
```

### Example Playlist ID
If the playlist URL is:
```
https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M
```
The playlist ID is:
```
37i9dQZF1DXcBWIGoYBM5M
```

## Customization
- **Delay Between API Calls:** You can adjust the delay between track queueing to prevent API rate limits.
- **Track Limit:** Modify the script to queue a specific number of tracks (useful for large playlists).

## Limitations
- Requires an active Spotify playback device (e.g., Spotify app open on a phone or desktop).
- Works only for playlists the authenticated user has access to.

## Contributions
Feel free to fork the repository and submit pull requests to improve the functionality or add new features.



