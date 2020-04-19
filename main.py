from __future__ import unicode_literals
import youtube_dl

from tkinter import *

def video_to_mp3(video_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([str(video_url)])





window = Tk()

window.title("YouTube to MP3")

window.geometry('350x200')

lbl = Label(window, text="video link:")

lbl.grid(column=0, row=0)

txt = Entry(window,width=10)

txt.grid(column=1, row=0)

def clicked():
    print(txt.get())
    video_to_mp3(txt.get())
    # res = "Welcome to " + txt.get()

    lbl.configure(text='video link:')

btn = Button(window, text="Make MP3", command=clicked)

btn.grid(column=2, row=0)

window.mainloop()

