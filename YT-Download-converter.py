from pytube import YouTube
import time
import sys
import os
import youtube_dl

print("\033[1;32;40m")
def banner():
    os.system('clear')
    time.sleep(1)
    print (" YOUTUBE VIDEO DOWNLOADER AND YOUTUBE VIDEO TO  MP3 CONVERTER ")
    time.sleep(1)
    print ("##########################################")
    time.sleep(1)
    print ( """
     _______________________________
     |                              |
     |  Coded by H3LL0-H4CK3R       |
     |  Thanks for using my tool    |
     |______________________________|\n""")
    time.sleep(1)
    print("############################################\n")
    time.sleep(1)

def load():
    def spinning_cursor():
        while True:
            for cursor in '|/-\\':
                yield cursor
    spinner = spinning_cursor()
    for _ in range(50):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

def downloadVideo():
    print("\033[1;32;40m")
    print("PROGRAM STARTED")
    time.sleep(1)
    print("DOWNLODE YOUTUBE VIDEOS WITH MY TOOL ")
    print("\033[1;31;40m")
    time.sleep(1)
    print("\033[1;32;40m")
    print("###################################")
    print("\033[1;32;40m")
    time.sleep(1)
    print("\033[1;32;40m")
    link = input("Enter Your Link Here :  ")
    print("\033[1;36;40m")
    print ("Please wait")
    time.sleep(1)
    print("\033[1;32;40m")
    print("Downloding...")
    YouTube(link).streams.first().download()
    print("\033[1;35;40m")
    print("Video downloaded successfully")
    time.sleep(1)
    print("\033[1;33;40m ")
    print("PROGRAM FINISHED")
    sys.exit(0)

def downloadMusic():
    print("\033[1;32;40m")
    print("PROGRAM STARTED")
    time.sleep(1)
    print("###################################")
    print("\033[1;36;40m")
    time.sleep(1)
    print("YOU CAN CONVERT YOUTUBE VIDEOS TO MP3  WITH MY TOOL ")
    print("\033[1;31;40m")
    time.sleep(1)
    print("###################################")
    print("\033[1;32;40m")
    time.sleep(1)
    link = input("Enter Your Link Here :  ")
    print("\033[1;36;40m")
    print ("Please wait")
    time.sleep(1)
    print("\033[1;32;40m")
    print("Converting...")

    params ={
        'format': 'bestaudio/best',
        'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'MP3',
            'preferredquality': '192',
        }],
        
    }

    youtube= youtube_dl.YoutubeDL(params)
    try:
        youtube.download([link])
    except:
        print("")
    time.sleep(1)
    print (" VIDEO TO MP3 CONVERTED SUCCESSFULLY ")
    time.sleep(1)
    print ("PROGRAM FINISHED ")
    sys.exit(0)

def main():
    banner()
    load()
    print("[1] YT VIDEO DOWNLOADER   [2] YT VIDEO TO MP3 CONVERTER ")
    print('')
    option=input('Enter the option : ')

    if option=='1' or option=='01':
        downloadVideo()
    elif option=='2' or option=='02':
        downloadMusic()
    else:
        print("\033[1;31;40m")
        print ('Invalid Option!')
        sys.exit(0)
    main()

main()

