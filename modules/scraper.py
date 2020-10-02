import requests
from bs4 import BeautifulSoup as bs
import re
import urllib.parse

def get_song_list(playlist_url):
    """
    This function get the song list in the form of "name creator" from the spotify page
    """

    # validating the data
    if not playlist_url.startswith("https://open.spotify.com"):
        print("this is not a spotify url")
        return []
    elif playlist_url == "https://open.spotify.com/collection/tracks":
        print("this app not support liked songs yet")
        return []

    try:
        html = requests.get(playlist_url)
    except Exception:
        print("invalid url")
        return []

    soup = bs(html.text, features="html.parser")

    # more data validation
    if soup.select('div.error'):
        print("invalid spotify url")
        return []

    # extracting the songs from the html file
    html_songs_list = soup.select('body div.tracklist-container ol li')

    songs_list = []
    for html_song in html_songs_list:
        song_name = html_song.select('span.track-name')[0].text
        song_creator = html_song.select('a span')[0].text
        songs_list.append(song_name + " " + song_creator)

    return songs_list


def find_video_url(song_name):
    """
    This function gets song name and search for the youtube video url
    """
    # This replacement is necesery because youtube does it 
    url_search_term = urllib.parse.quote(song_name).replace("%20", "+")

    html_search_results = requests.get("https://www.youtube.com/results?search_query="+url_search_term)
    soup = bs(html_search_results.text, features="html.parser")

    # The second script in the page has all the results
    data = soup.select('body script')[1]

    # That was the only way i succeed to get the content of the script .text did not work
    script = str(data.string)

    # this unbelivible short regex return all the youtube results urls suffixes
    urls_sufixes = re.findall(r'/watch(.*?)"', script)
    wanted_url = "https://www.youtube.com/watch" + urls_sufixes[0]
    return wanted_url
