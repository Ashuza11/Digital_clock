from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Ash Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string) # Call the time in the label
    label.after(1000, time)

# Settings
label = Label(root, font = ("DS-digital", 80), background = "black", foreground = "cyan")
label.pack(anchor = 'center') # location on the window

time()
mainloop()