import requests
import os

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': os.environ.get('e4965faf38934e828c4c80ac81cade44'),
    'client_secret': os.environ.get('ff126b2cb4bb4ff0a2522fe7f305daae'),
})

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']

headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

BASE_URL = 'https://api.spotify.com/v1/'

track_url = input('Enter track URL: ')
track_id = track_url.split('/')[-1]

r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
track_data = r.json()

print(track_data)

# Function to recommend tracks based on a seed track ID
def recommend_tracks(seed_track_id):
    endpoint = 'recommendations'
    params = {
        'seed_tracks': seed_track_id,
        'limit': 5  # Number of tracks to recommend
    }
    r = requests.get(BASE_URL + endpoint, headers=headers, params=params)
    recommendation_data = r.json()
    
    # Print out recommended track names
    print("Recommended tracks:")
    for track in recommendation_data['tracks']:
        print(track['name'])

# Example usage: recommend tracks based on the first track ID
recommend_tracks('6mFkJmJqdDVQ1REhVfGgd1')