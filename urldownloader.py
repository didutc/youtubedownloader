
import io
import json
import os
import sys
import time
from bs4 import BeautifulSoup
import argparse
import lxml.html
import requests as re
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from subprocess import call
import youtube_dl
import tkinter
from tkinter import filedialog
root = tkinter.Tk()
root.withdraw()

print('url입력')
url = input()
url = url.split('\n')
if type(url) == list:
    print(1)

# root.call('wm', 'attributes', '.', '-topmost', True)
# dir_path = filedialog.askdirectory(
#     parent=root,initialdir="/",title='Please select a directory')

# try:
#     if url == 'txt':
#         url = open("./url.txt", 'r', -1, "utf-8")
#         data = url.read()

#         url = data.split('\n')

#         for li in url:
#             print(dir_path+'%(title)s.%(ext)s')
#             ydl_opts = {
#                 'format': 'worstaudio/best',
#                 'outtmpl': dir_path+'%(title)s.%(ext)s',
#                 'postprocessors': [{
#                     'key': 'FFmpegExtractAudio',
#                     'preferredcodec': 'mp3',
#                     'preferredquality': '320',
#                 }],
#             }
#         print(ydl_opts)
#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([li])
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
# except:
#     print('wrongworld')
#     print(dir_path+'%(title)s.%(ext)s')
#     ydl_opts = {
#         'format': 'worstaudio/best',
#         'outtmpl': dir_path+'/%(title)s.%(ext)s',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '320',
#         }],
#     }

#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])