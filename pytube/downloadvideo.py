from pytube import YouTube
import sys

# URL del video de YouTube
if len(sys.argv) == 2:
    video_url = sys.argv[1]
    print("url:", video_url)
else:
    exit()

yt = YouTube(video_url)
print(len(yt.streams))

#video = yt.streams.get_highest_resolution()


#video.download()

print("✅ Video descargado con éxito!")
