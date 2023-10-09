import requests
from googleapiclient.discovery import build
api_key="AIzaSyDxQkZ1ik7V9uMZ4QaH3GQFcnIlySU2BBI"
youtube=build("youtube",'v3',developerKey=api_key)


def get_video_id(link:str)->str:
    i=link.find("watch?v=")
    link=link[i+8:]
    return link

def get_page_data(videoid:str,next_page_token=None):
    request=youtube.commentThreads().list(part='snippet',videoId=videoid,maxResults=100,textFormat='plainText',pageToken=next_page_token)
    response=request.execute()
    return response


def fetch_comments(response,data):
    for item in response.get('items'):
        obj=item.get('snippet').get('topLevelComment')
        name=obj.get('snippet').get('authorDisplayName')
        comment=obj.get('snippet').get('textDisplay')
        # data.append((name,comment))
        data["Username"].append(name)
        data["Comment"].append(comment)
    next_page_token=response.get('nextPageToken')
    return (next_page_token)

def get_data(link:str,data:list,pageToken=None)->list:
    try:
        videoid=get_video_id(link)
        response=get_page_data(videoid,pageToken)
        next_page_token=fetch_comments(response,data)
        if(len(data["Username"])>1000):
            return
        else:
            get_data(link,data,next_page_token)
    except Exception as e:
        return