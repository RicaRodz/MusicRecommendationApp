import requests
import base64
import pandas as pd
from musicData import get_trending_playlist_data

# Replace with your own Client ID and Client Secret
CLIENT_ID = 'd0a05b1bc0d44c23ae0cd6dff22dc515'
CLIENT_SECRET = '8692cb67a5254679a8e9a30e7b89ac0f'

# Base64 encode the client ID and client secret
client_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
client_credentials_base64 = base64.b64encode(client_credentials.encode()).decode()

# Request the access token
token_url = 'https://accounts.spotify.com/api/token'
headers = {
    'Authorization': f'Basic {client_credentials_base64}'
}
data = {
    'grant_type': 'client_credentials'
}
response = requests.post(token_url, data=data, headers=headers)

if response.status_code == 200:
    access_token = response.json().get('access_token')
    print("Access token obtained successfully.")
else:
    print(f"Error obtaining access token. Status code: {response.status_code}")
    exit()

# Verify if the access token is obtained before proceeding
if not access_token:
    print("Access token not available. Exiting.")
    exit()

# Replace with your actual playlist ID
playlist_id = '37i9dQZF1DX76Wlfdnj7AP'

# Call the function to get the music data from the playlist and store it in a DataFrame
music_df = get_trending_playlist_data(playlist_id, access_token)

# Verify if the DataFrame is not empty before saving to Excel
if not music_df.empty:
    # Save to Excel
    file_path_excel = '/Users/ricardordoriguez/Desktop/Github/MusicRecomApp/MusicRecommendationApp/hybrid_recommendations.xlsx'
    music_df.to_excel(file_path_excel, index=False)
    print("DataFrame saved to Excel successfully.")
else:
    print("DataFrame is empty. No data to save.")

