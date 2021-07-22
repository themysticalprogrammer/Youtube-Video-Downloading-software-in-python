from pytube import YouTube

link = "" # Write Link here

try:
    youtubeLinkObj = YouTube(link)

except:
    print("Connection Error !!!")

try:
    print("Downloading of the video has been started")
    youtubeLinkObj.streams.first().download()
    print("Downloading of the video has been completed")

except:
    print("Some Error while Downloading occured !!!!!")