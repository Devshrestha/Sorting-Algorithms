import tkinter as gui
from tkinter import ttk
from sorting import sort

a=[]
b=[]
arr=[]
i=0
en=True

root= gui.Tk()
frame=ttk.Frame(root).grid()
text=ttk.Label(text='Enter elments')
text.grid(row=1,column=1)

def last_entry():
    en = False


def arry_entry(i):
    def on_change():
        
        try:
            b.append(float(a[i-1].get()))
        except ValueError:
            print('error')
        if float(b[i-1])==int(b[i-1]):
            arr.append(int(b[i-1]))
            
        elif type(b[i-1])==float:
            arr.append(float(b[i-1]))
        

                

    if en:
        a.append(None)
        a[i]=ttk.Entry()
        a[i].grid(row=2,column=i+1)
        a[i].focus()
        i+=1
        root.bind('<Return>',lambda event:on_change())
        root.bind('<KeyRelease-Return>',lambda event:arry_entry(i))
 
def xx():
    if not en:
        print(arr)
arry_entry(i)
confirm=ttk.Button(text="Proceed",command=last_entry).grid(row=3,column=1)

bubble=ttk.Button(text="Bubble-Sort",command=lambda:s.bubble_sort(arr))
bubble.grid(row=4,column=1)

s=sort()
gui.mainloop()