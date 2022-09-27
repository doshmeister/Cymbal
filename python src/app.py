from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Feet to Meters")

feet = StringVar()
feet_entry = ttk.Entry(mainframe,width=7,textvariable=feet)
feet_entry.grid(column=2,row=1, sticky=(W,E))

meters = StringVar()
ttk.Label(mainframe,textvariable=meters).grid(column=2,row=2,sticky=(W))

