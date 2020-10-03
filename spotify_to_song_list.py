from modules.scraper import get_song_list, find_video_url
from modules.youtube_downloader import download_song

__author__ = "https://github.com/nofearOnline"


def main():
    url = input("Enter playlist url: ")
    song_list = get_song_list(url)

    if not song_list:
        print("you can always try again :)")
        return

    for song in song_list:
        song_url = find_video_url(song)
        try:
            download_song(song_url)
        except:
            continue

    print("Thanks for using my script :)")


if __name__ == "__main__":
    main()
