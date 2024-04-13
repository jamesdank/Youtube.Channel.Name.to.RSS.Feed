# Import the required libraries
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up the API client
api_key = ""
youtube = build('youtube', 'v3', developerKey=api_key)

channel = input("Enter channel name: ")

# Get the channel ID
channel_name = channel
request = youtube.search().list(q=channel_name, type='channel', part='id', maxResults=1)
response = request.execute()
channel_id = response['items'][0]['id']['channelId']

# Use the channel ID to get the channel statistics
request = youtube.channels().list(part='statistics', id=channel_id)
response = request.execute()

# Print the statistics
print(f"\nChannel name: {channel_name}")
print(f"RSS Feed: https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}")