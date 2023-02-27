import time
lis ='fsdfsdfsdfW'
from pytube import Playlist
import youtube_dl
import tkinter
from tkinter import filedialog
import doubleagent
root = tkinter.Tk()
root.withdraw()

playl = input('입력해 주세요:')


root.call('wm', 'attributes', '.', '-topmost', True)
dir_path = filedialog.askdirectory(
    parent=root,initialdir="/",title='Please select a directory')

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': dir_path+'/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playl])
