import json
import requests
from config import *
from urllib.parse import quote

def get_recent(user):
    try:
        print("start")
        url = f"{api_root}?method=user.getrecenttracks&user={quote(user)}&api_key={quote(API_KEY)}&format=json&limit=1"
        print("req",url)
        request = requests.get(url)
        request.raise_for_status()
        print("after reg")
        return json.loads(request.text)["recenttracks"]["track"][0], json.loads(request.text)
    except Exception as e:
        print(f"Error: {e}")
        return None
def get_song_name(data):
    return data["name"]

def get_artist(data):
    return data["artist"]["#text"]
    
def get_image_url(data):
    
    return data["image"][3]["#text"]

def get_album(data):
    return data["album"]["#text"]

def get_date(raw):
    return raw["recenttracks"]["track"][1]["date"]["uts"]

def check_playing(data):
    try:
        data["@attr"]["nowplaying"]
        return True
    except KeyError:
        return False