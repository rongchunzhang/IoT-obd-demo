#!/usr/bin/python

from Tkinter import *
##from Tkinter import tTk
import tkFont
import time
import os
import thread

def quit(*args):
    fo.close()
    root.destroy()

fo = open('SPEED',"r")

def show_time():
    while True:
        fo.seek(0,0)
        data = fo.read(8)
        txt.set(data)
        print(data)
        # Trigger the countdown after 1000ms
        #root.after(100, show_time)
        time.sleep(0.5)

# Use tkinter lib for showing the clock
root = Tk()
root.attributes("-fullscreen", True)
##root.attributes('-zoomed', True)
root.configure(background='black')
root.bind("<Control-x>", quit)
##root.after(100, show_time)
fnt = tkFont.Font(family='Helvetica', size=160, weight='bold')
txt = StringVar()
lbl = Label(root, textvariable=txt, font=fnt, foreground="white", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

thread.start_new_thread(show_time,())

root.mainloop()
