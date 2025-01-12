import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import pandas as pd
import time

# Load environment variables
load_dotenv()

# Replace with your own Client ID and Client Sejcret
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

# Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Load the CSV file
data = pd.read_csv("backend/db/raw_data/top_10000_1950-now.csv")

# Ensure the DataFrame has the necessary columns
if 'Track URI' not in data.columns:
    raise ValueError("The CSV file must contain a 'Track URI' column.")
if 'Album Cover URL' not in data.columns:
    data['Album Cover URL'] = None

# Process only rows where 'Album Cover URL' is missing
rows_to_process = data[data['Album Cover URL'].isnull()]

print(f"Processing {len(rows_to_process)} rows without album cover URLs.")

# Iterate through the rows
for index, row in rows_to_process.iterrows():
    track_uri = row['Track URI']
    
    try:
        # Fetch track information
        track_info = sp.track(track_uri)
        
        # Get album information
        album_info = track_info['album']
        
        # Extract album cover URL
        album_cover_url = album_info['images'][0]['url'] if album_info['images'] else None
        
        # Update the DataFrame
        data.at[index, 'Album Cover URL'] = album_cover_url
        
        # Debug information
        print(f"Processed: {track_info['name']} by {track_info['artists'][0]['name']}")
    
    except Exception as e:
        print(f"Error fetching album cover for URI {track_uri}: {e}")
    
    # Handle API rate limits (pause after every 50 requests)
    if index % 50 == 0:
        print("Pausing for rate limit...")
        time.sleep(5)  # Adjust sleep time as needed

# Save the updated data to a new CSV file once all rows are processed
output_file = "backend/db/raw_data/top_10000_1950-now_with_covers.csv"
data.to_csv(output_file, index=False)

print(f"Updated data saved to {output_file}")
