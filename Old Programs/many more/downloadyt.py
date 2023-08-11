from pytube import YouTube

path="C:/Users/Hites/Desktop/Python/ytvides"

link=input("Enter link: ")

yt=YouTube(link)

print("view:",yt.views)

yd=yt.streams.get_highest_resolution()

yd.download(path)
