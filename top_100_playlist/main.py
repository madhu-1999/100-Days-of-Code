from datetime import datetime
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BASE_URL = 'https://www.billboard.com/charts/hot-100/'
CLIENT_ID = '86b15a95c35a4dcc9b9ff02568f07f96'
CLIENT_SECRET='52a6455f5b5e4e21a2e6db4f510e26d3'
def validate_date(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        return False

def __main__():
    date  = input("Enter date in format YYYY-MM-DD: ")
    if validate_date(date) :
        response = requests.get(BASE_URL+date)
        soup = BeautifulSoup(response.content, "html.parser")
        chart_items = soup.find_all('li',class_='o-chart-results-list__item')
        songs = [title.text.strip() for item in chart_items for title in item.find_all('h3',id='title-of-a-story')]
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri="http://example.com",
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                show_dialog=True,
                cache_path="token.txt"
            )
        )
        user_id = sp.current_user()["id"]
        song_uris = []
        year = date.split("-")[0]
        for song in songs:
            result = sp.search(q=f"track:{song} year:{year}", type="track")
            print(result)
            try:
                uri = result["tracks"]["items"][0]["uri"]
                song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")

__main__()