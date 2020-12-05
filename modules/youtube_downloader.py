from __future__ import unicode_literals
import youtube_dl

# This function download the song from youtube using youtube_dl which comes on top of ffmpeg
def download_song(song_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'music/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }],
        
        'prefer_ffmpeg': True
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([song_url])
