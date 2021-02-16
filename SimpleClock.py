# Simple Clock
from Tkinter import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font = ("Arial", 80), bg = "black", fg = "cyan")
label.pack(anchor='center')

time()
mainloop() 
