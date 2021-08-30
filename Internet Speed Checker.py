# pip install pyspeedtest
from tkinter import *
from tkinter import messagebox
import pyspeedtest


def one():
    speed = pyspeedtest.SpeedTest("www.google.com")
    a1 = (str(speed.download()) + " [ Bytes per second ]")
    messagebox.showinfo("Your download speed : ", a1)


root = Tk()
root.title("INTERNET SPEED CHECKER")
root.config(bg="pink")  # to set the bg color
#root.geometry("500x400")
root.geometry("500x250")

label1 = Label(root, text="Internet Speed Checker", font=("arial", 30, "bold"),
               bg="lightblue").pack()  # pack() will allow to put these line by line
button1 = Button(root, text="Click !!", font=("arial", 20, "bold"), bg="yellow",height=1,width=10,command=one).pack()

root.mainloop()