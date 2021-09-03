# GUI
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilenames, asksaveasfilename


def open_file():
    filepath = askopenfilenames(
        filetypes=[("Text files","*.txt"),("All files","*.*")])
    if not filepath:
        return     # if file is not in any of two extensions
    text_edit.delete(1.0,tk.END)
    # file handling for opening the file
    with open(filepath,"r") as input_file:    # open the file entered by user
        text = input_file.read()
        text_edit.insert(tk.END, text)

    # name of the window
    window.title(f"My Own Writing Space - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt", filetypes=[("Text files","*.txt"),("All files","*.*")])    # if forget to provide extension
    if not filename:
        return
    with open(filepath,"w") as output_file:
        text = text_edit.get(1.0, tk.END)
        output_file.write(text)
    # title to window
    window.title(f"My Own Writing Space - {filepath}")

window = tk.Tk()
window.title("My Own Writing Space")
window.rowconfigure(0, minsize=800, weight=1)    # cursor will strat frm 0
window.columnconfigure(1, minsize=800, weight=1)

text_edit = tk.Text(window)
fr_buttons = tk.Frame(window,relief=tk.RAISED, bd=2)
#button_new = tk.Button(fr_buttons, text="NEW WINDOW", command=openNewWindow())
button_open = tk.Button(fr_buttons, text="OPEN", command=open_file)
button_save = tk.Button(fr_buttons, text="SAVE AS...", command=save_file)
button_exit = tk.Button(fr_buttons, text="EXIT!!", command=lambda:exit())

button_open.grid(row=0, column=0, sticky="ew", padx=5, pady= 5)
button_save.grid(row=1, column=0, sticky="ew", padx= 5)
button_exit.grid(row=2, column=0, sticky="ew", padx= 5)
#button_new.grid(row=3,column=0, sticky="ew", padx= 5)

fr_buttons.grid(row=0, column=0, sticky="ns")
text_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
