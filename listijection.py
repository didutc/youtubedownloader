from pytube import Playlist
import youtube_dl
import tkinter
from tkinter import filedialog
import doubleagent
from alive_progress import alive_bar

 
root = tkinter.Tk()
root.withdraw()

f = open('listinjection.txt', 'r', -1, "utf-8")
data = f.read()
f.close()

while True:
    if data[-1] == "\n":
        data = data[:-1]
    else:
        break
pl = data.split('\n')


root.call('wm', 'attributes', '.', '-topmost', True)
dir_path = filedialog.askdirectory(
    parent=root,initialdir="/",title='Please select a directory')
with alive_bar(len(pl)) as bar:   
    for url in pl:          
        bar()       
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': dir_path+'/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as ex:

            if "Forbidden" in str(ex):
                pl.append(url)
