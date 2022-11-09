import pytube 

link = input("Please paste your link here: ")
yt = pytube.YouTube(link)
audio = yt.streams.filter(only_audio=True)
audio[0].download()
print("Your audio has been downloaded! ")