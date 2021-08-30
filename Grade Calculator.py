# GUI Project
import tkinter     # all the GUI projects in python are made using tkinter library
from tkinter import *    # * means import each n everything

root = Tk()     # tk() is tkinter lib, a new tkinter window will be coming here
root.title("GRADE CALCULATOR")     # title of window
root.geometry("500x400")      # configuration of the window

def marks_calculate():
    maths = int(maths_value.get())
    science = int(science_value.get())
    computer = int(computer_value.get())
    final = (maths+science+computer)
    Label(text=f"{final}", font="arial 20 bold").place(x=250,y=170)# to print something on tkinter window

    average =int(final/3)
    Label(text=f"{average}", font="arial 20 bold").place(x=250,y=220)

    if (average>50):
        grade_score = "PASS!! :)"
    else:
        grade_score = "FAIL!! :("

    Label(text=f"{grade_score}", font="arial 20 bold").place(x=250,y=270)

# diff labels for diff subjects
sub_1 = Label(root, text="Maths : ", font="arial 20")
sub_1.place(x=50,y=20)
sub_2 = Label(root,text="Science : ", font="arial 20")
sub_2.place(x=50,y=70)
sub_3 = Label(root,text="Computer : ", font="arial 20")
sub_3.place(x=50,y=120)
#sub_2 = Label(root,text="Science", font="arial 20")
#sub_2.place(x=50,y=70)
total_marks = Label(root,text="Total", font="arial 20")
total_marks.place(x=50,y=170)
average_marks = Label(root,text="Average", font="arial 20")
average_marks.place(x=50,y=220)
grade_score = Label(root,text="Grades", font="arial 20")
grade_score.place(x=50,y=270)

maths_marks = StringVar()
science_marks = StringVar()
computer_marks = StringVar()

# to create box and take user input
maths_value = Entry(root, textvariable = maths_marks, font="arial 20", width=50)
maths_value.place(x=250,y=20)
science_value = Entry(root, textvariable =science_marks, font="arial 20", width=50)
science_value.place(x=250,y=70)
computer_value = Entry(root, textvariable = computer_marks, font="arial 20", width=50)
computer_value.place(x=250,y=120)

# for creating buttons
Button(text="Calculate", font="arial 15", bg="blue",bd=5,command=marks_calculate).place(x=50,y=330)
Button(text="Exit", font="arial 15", bg="red",bd=5,width=8,command=lambda:exit()).place(x=350,y=330)

root.mainloop()    # to close the whole program
