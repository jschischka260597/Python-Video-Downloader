#Enter a youtube link to download video

from pytube import YouTube

def main():
    downloader()
    
def downloader():
    try:
        url = input("Enter the link: ")

        yt = YouTube(url)
        
        yt.streams.get_highest_resolution().download("Videos")

        print("Download Completed")

    except:
        print("Invalid link")
        downloader()

main()
