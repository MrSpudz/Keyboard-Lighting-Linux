from distutils.command.build import build
from tkinter import *
import os

windowname = "Keyboard LED Controller V1.0.0"

def ON():
   os.system('xset led on')

def OFF():
    os.system('xset led off')

window = Tk()
window.title(windowname)
window.geometry('1920x1080')
window.config(bg='white')

offImg = PhotoImage(file="off.png")
onImg = PhotoImage(file="on.png")

label = Label(
    window,
)
label.place(x=0, y=0)

button =Button(window,
    text="On",
    command=ON,
    image=onImg
)
button.pack()

button =Button(window,
    text="off",
    command=OFF,
    image=offImg
)
button.pack()

print("Program started")

window.mainloop()

print("Program ended")