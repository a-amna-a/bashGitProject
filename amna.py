from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os
import json

# Define the scopes required
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

# Path to the video file you want to upload
video_file_path = 'path_to_your_video_file.mp4'

# Function to authenticate and obtain credentials
def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secrets.json', SCOPES)
    credentials = flow.run_console()
    return build('youtube', 'v3', credentials=credentials)

# Upload video function
def upload_video(youtube, video_file, title, description):
    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': ['youtube', 'python', 'tutorial']
        },
        'status': {
            'privacyStatus': 'private'  # Change as needed
        }
    }

    media = MediaFileUpload(video_file, chunksize=-1, resumable=True)

    response = youtube.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=media
    ).execute()

    print(f"Video uploaded! Video ID: {response['id']}")

if __name__ == "__main__":
    # Authenticate and get the service
    youtube_service = get_authenticated_service()

    # Call the upload_video function
    upload_video(youtube_service, video_file_path, 'Test Video', 'This is a test video uploaded using YouTube API')
