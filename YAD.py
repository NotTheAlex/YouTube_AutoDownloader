import os
from threading import Thread
import pyperclip

def toURL(url):
    if '&list' in url:
        tmp = url.split('&list=')
        url = 'https://www.youtube.com/playlist?list=' + tmp[-1]
    return url


def download(url):
    os.system ('pytube ' + toURL (url))

if __name__ == '__main__':
    temp_url = ''
    url = ''
    while True:
        url = pyperclip.paste()
        if url != temp_url and 'youtube.com' in url:
            temp_url = url
            Thread(target=download, args=(url)).start()