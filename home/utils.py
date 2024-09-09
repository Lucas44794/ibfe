from googleapiclient.discovery import build

def get_live_video_id(channel_id):
    api_key = 'YOUR_API_KEY'
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(
        part='id',
        channelId=channel_id,
        eventType='live',
        type='video'
    )
    response = request.execute()
    if response['items']:
        return response['items'][0]['id']['videoId']
    return None