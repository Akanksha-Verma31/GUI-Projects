from tkinter import *
from pytube import YouTube
tk_window = Tk()  #tkinter window
tk_window.geometry("600x700")
tk_window.config(bg="black")
tk_window.title("MY YOUTUBE VIDEO DOWNLOADER !!")

Label(tk_window, text="VIDEO DOWNLOADER", font=("Arial", 38, "bold"), bg="black", fg="yellow").pack(padx=5, pady=50)

l_video = StringVar()
Label(tk_window, text=" Enter the link : ", font=("Arial",26,"bold"), bg="light blue", fg="black").place(x=170, y=145)
l_entry = Entry(tk_window, width=50, font=34, textvariable=l_video, bd=4).place(x=20, y=200)

def d_video():
    url_v = YouTube(str(l_video.get()))
    videos = url_v.streams.first()
    videos.download()

    Label(tk_window, text="Video Downloaded", font=("Arial", 25, "bold"), bg="light pink", fg="black").place(x=120, y=450)


Button(tk_window, text="Download", font=("Arial",25,"bold"), bg="white", fg="red", command=d_video).place(x=180, y=300)


tk_window.mainloop()