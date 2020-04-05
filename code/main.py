import tkinter as gui
from tkinter import *
from tkinter import ttk


root= gui.Tk()
frame=ttk.Frame(root).grid()
text=ttk.Label(text='Enter no elements').grid(row=1,column=1)
n=ttk.Entry().grid(row=1,column=2)

#print(n.get())
def exit():
    en = False
a=[]
i=0
en=True
while i<5:
    a.append(None)
    a[i]=ttk.Entry().grid(row=2,column=i+1)
    i+=1
confirm=ttk.Button(text="Enter",command=lambda:exit()).grid(row=2,column=i+2)




gui.mainloop()