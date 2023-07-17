import os.path
import pandas as pd

from pytube import YouTube
Musicas = pd.read_excel('Musicas.xlsx')
for i, Link in enumerate(Musicas['Link']):
    yt = YouTube(Link)
    video = yt.streams.filter(only_audio=True).first()
    download_file = video.download()
    base, ext = os.path.splitext(download_file)
    new_file = base + ".mp3"
    os.rename(download_file, new_file)
    print('É os guri!')