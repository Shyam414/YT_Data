from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns
from IPython.display import JSON

api_key = input("Please enter your YouTube Data API key: ")
channel_ids=['UCX6OQ3DkcsbYNE6H8uQQuVA',
             'UCChmJrVa8kDg05JfCmxpLRw',
             'UCkX0NXCP9kCLtk30kjTXIWg',
             'UCXqJrBG563pZnaqLoxHjUDg',
             'UCHoLIMtg_OigNlJmjHX9J8Q',
             'UCMOLiZpKXp-w5CNfqJObQUw',
             'UCtAXJ4DNpshfVjLIMq9pIRw']

youtube= build('youtube','v3',developerKey=api_key)

def get_channel(youtube,channel_ids):
    
    all_data = []
    request = youtube.channels().list(
                part='snippet,contentDetails,statistics',
                id=','.join(channel_ids)
                )
    response = request.execute() 
    

    for i in range(len(response['items'])):
        data = dict(channelName = response['items'][i]['snippet']['title'],
                    subscribers = response['items'][i]['statistics']['subscriberCount'],
                    views = response['items'][i]['statistics']['viewCount'],
                    totalVideos = response['items'][i]['statistics']['videoCount'],
                    playlistId = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
        all_data.append(data)
    
    return pd.DataFrame(all_data)


channel_stats=get_channel(youtube,channel_ids)
channel_stats

playlist_id='UUX6OQ3DkcsbYNE6H8uQQuVA'
def get_video_ids(youtube, playlist_id):
    video_ids = []

    request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId = playlist_id,
                maxResults = 50)
    response = request.execute()
    
    
    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])
        
    next_page_token = response.get('nextPageToken')
    more_pages = True
    
    while more_pages:
        if next_page_token is None:
            more_pages = False
        else:
            request = youtube.playlistItems().list(
                        part='contentDetails',
                        playlistId = playlist_id,
                        maxResults = 50,
                        pageToken = next_page_token)
            response = request.execute()
    
            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])
            
            next_page_token = response.get('nextPageToken')
        
    return video_ids


Video_ids=get_video_ids(youtube, playlist_id)
len(Video_ids)



def get_video_details(youtube, video_ids):    
    all_video_info = []
    
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=','.join(video_ids[i:i+50])
        )
        response = request.execute() 

        for video in response['items']:
            stats_to_keep = {'snippet': ['channelTitle', 'title', 'description', 'tags', 'publishedAt'],
                             'statistics': ['viewCount', 'likeCount', 'favouriteCount', 'commentCount'],
                             'contentDetails': ['duration', 'definition', 'caption']
                            }
            video_info = {}
            video_info['video_id'] = video['id']

            for k in stats_to_keep.keys():
                for v in stats_to_keep[k]:
                    try:
                        video_info[v] = video[k][v]
                    except:
                        video_info[v] = None

            all_video_info.append(video_info)
            
    return pd.DataFrame(all_video_info)

videoDetails=get_video_details(youtube, Video_ids)
videoDetails

def get_comments_in_videos(youtube, video_ids):
    all_comments = []
    
    for video_id in video_ids:
        try:   
            request = youtube.commentThreads().list(
                part="snippet,replies",
                videoId=video_id
            )
            response = request.execute()
        
            comments_in_video = [comment['snippet']['topLevelComment']['snippet']['textOriginal'] for comment in response['items'][0:10]]
            comments_in_video_info = {'video_id': video_id, 'comments': comments_in_video}

            all_comments.append(comments_in_video_info)
            
        except: 
            # When error occurs - most likely because comments are disabled on a video
            print('Could not get comments for video ' + video_id)
        
    return pd.DataFrame(all_comments)  

comments=get_comments_in_videos(youtube, Video_ids)
comments

videoDetails.to_csv('Data\\apiData.csv', index=False)
comments.to_csv('Data\\commentsData.csv', index=False)

