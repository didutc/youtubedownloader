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

def playlist():
    playlist = []
    YOUTUBE_VIDEO_URL = 'https://www.youtube.com/channel/UCqbpna45EO7qaARGv2vgjkg/videos'

    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
    session = re.session()
    res = session.get(YOUTUBE_VIDEO_URL, headers=headers)
    redirect_cookie = res.headers['Set-Cookie']
    soup = BeautifulSoup(res.text, 'html.parser')
    foler_name = soup.find("title")
    foler_name = foler_name.text
    array_res = []
    res = res.text
    path = foler_name

    try:
        os.mkdir(path)
    except:
        pass
    dir_path = os.getcwd()
    slash = '\\'
    foler_path = dir_path+slash+path+slash

    foler_path.replace('\\', '/')
    f = open("./text.html", 'w', -1, "utf-8")
    f.write(res)
    res = res.split(',')

    f.close()
    try:
        for al in res:
            if '{"continuation":"' in al:
                continuation = al

        continuation = continuation[58:]
        continuation = continuation[:-6]

        for be in res:
            if '"clickTrackingParams":"' in be and not '=' in be:
                clickTrackingParams = be
        print(clickTrackingParams)

        clickTrackingParams = clickTrackingParams[34:]
        clickTrackingParams = clickTrackingParams[:-4]
        clickTrackingParams = clickTrackingParams[1:]
        platlist_Url = 'https://www.youtube.com/browse_ajax?ctoken=' + \
            str(continuation)+'253D%253D&continuation=' + \
            str(continuation)+'253D%253D&itct=' + \
            str(clickTrackingParams)+''
        print(clickTrackingParams)
        input()
        params = {
            'ctoken': continuation,
            'continuation:': continuation,
            'itct': clickTrackingParams

        }
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
            'x-youtube-client-name': '1',
            'x-youtube-client-version': '2.20200821.01.00',
            'x-client-data': 'CIu2yQEIprbJAQjEtskBCKmdygEI2qHKAQiGtcoBCJm1ygEI/7zKAQjnxsoBCPjHygEI58jKAQjpyMoBCLTLygEIltbKAQi818oB'
        }
        res = session.get(platlist_Url, headers=headers, params=params)
        print(platlist_Url)
        print(clickTrackingParams)
        print('좆됌')

        input()
        playlist.append(res)

        num = 0
        while True:
            array_res = []
            res = res.text

            res = res.split(',')
            for al in res:
                if '{"continuation":"' in al:
                    continuation = al
            continuation = continuation[58:]
            continuation = continuation[:-6]
            if len(continuation) < 40:
                break

            for be in res:
                if '"clickTrackingParams":"' in be and not '=' in be:
                    clickTrackingParams = be
            clickTrackingParams = clickTrackingParams[23:]
            clickTrackingParams = clickTrackingParams[:-4]

            print(clickTrackingParams)

            platlist_Url = 'https://www.youtube.com/browse_ajax?ctoken=' + \
                str(continuation)+'253D%253D&continuation=' + \
                str(continuation)+'253D%253D&itct=' + \
                str(clickTrackingParams)+''

            params = {
                'ctoken': continuation,
                'continuation:': continuation,
                'itct': clickTrackingParams

            }
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
                'x-youtube-client-name': '1',
                'x-youtube-client-version': '2.20200821.01.00',
                'x-client-data': 'CIu2yQEIprbJAQjEtskBCKmdygEI2qHKAQiGtcoBCJm1ygEI/7zKAQjnxsoBCPjHygEI58jKAQjpyMoBCLTLygEIltbKAQi818oB'
            }
            print(platlist_Url)

            res = session.get(platlist_Url, headers=headers, params=params)

            time.sleep(1)
            num = num + 1
            playlist.append(res)

        good_list = []
        print(playlist)
        for be in playlist:
            res = be
            res = res.text
            res = res.split(',')
            for al in res:
                if '"commandMetadata":{"webCommandMetadata":{"url":"' in al and not 'service_ajax' in al and not 'endpoint' in al:
                    al = al.replace(
                        '"commandMetadata":{"webCommandMetadata":{"url":"', '')
                    al = al.replace('"', '')
                    good_list.append(al)

        print(len(good_list))

        print(foler_path)
        ydl_opts = {
            'format': 'worstaudio/best',
            'outtmpl': ''+foler_path+'%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        for gam in good_list:
            url = 'https://www.youtube.com/'+str(gam)+''
            print(url)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

    except Exception as e:
        print(e)
        goods_list = []
        res = session.get(YOUTUBE_VIDEO_URL)
        res = res.text
        res = res.split(',')
        for li in res:
            if 'createPlaylistServiceEndpoint":{"videoIds":' in li:
                li = li.replace(
                    '"createPlaylistServiceEndpoint":{"videoIds":["', '')
                li = li[:-2]
                goods_list.append(li)
        goods_list = list(set(goods_list))
        good_list = []
        for li in goods_list:
            url = 'https://www.youtube.com/watch?v='+li+''
            good_list.append(url)
        print(good_list)
        ydl_opts = {
            'format': 'worstaudio/best',
            'outtmpl': ''+foler_path+'%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        for gam in good_list:
            url = gam
            print(url)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])


def url_downloader():
    print('url입력')
    url = input()

    root.call('wm', 'attributes', '.', '-topmost', True)
    dir_path = filedialog.askdirectory(
        parent=root,initialdir="/",title='Please select a directory')

    try:
        if url == 'txt':
            url = open("./url.txt", 'r', -1, "utf-8")
            data = url.read()

            url = data.split('\n')

            for li in url:
                print(dir_path+'%(title)s.%(ext)s')
                ydl_opts = {
                    'format': 'worstaudio/best',
                    'outtmpl': dir_path+'%(title)s.%(ext)s',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '320',
                    }],
                }
            print(ydl_opts)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([li])
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except:
        print('wrongworld')
        print(dir_path+'%(title)s.%(ext)s')
        ydl_opts = {
            'format': 'worstaudio/best',
            'outtmpl': dir_path+'/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])


def videodownload():
    print('url입력')
    url = input()

    call('youtube-dl -F '+url + '')
    print('품질선택')
    qc = input()
    call('youtube-dl -f'+qc+' '+url + '')


while True:
    print('1: 플레이리스트 다운 2: url다운로드 3:영상다운로드')
    print()
    userinput = input()
    if userinput == '1':
        playlist()
    if userinput == '2':
        url_downloader()
    if userinput == '3':
        videodownload()
    if userinput == 'out':
        break
