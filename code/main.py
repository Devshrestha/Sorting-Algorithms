import tkinter as gui
from tkinter import ttk
import random
from sorting import sort

a=[]
b=[]
arr=[]
i=0
en=True

root= gui.Tk()
frame=ttk.Frame(root).grid()
v=None


def run_manual():
    text=ttk.Label(text='Enter elments')
    text.grid(row=1,column=1)
    arry_entry(i)
    confirm=ttk.Button(text="Proceed",command=last_entry)
    confirm.grid(row=3,column=1)


def run_random():
    


    def generate():
        r=[]
        inp=[]
        for a in [no,first,last]:
            try:
                inp.append(float(a.get()))
                
            except ValueError:
                return
        if inp[1]>inp[2]:
            temp=inp[2]
            inp[2]=inp[1]
            inp[1]=temp
        
        for i in range(int(inp[0])):
            r.append(None)        
            arr.append(random.randrange(inp[1],inp[2]))
            r[i]=ttk.Label(text=arr[i]).grid(row=4,column=i+1)
        
        
             
    no_label=ttk.Label(text='no of elements').grid(row=1,column=1)
    no=ttk.Entry()
    no.focus()
    f=1
    no.grid(row=1,column=2)
    
    first_label=ttk.Label(text='First element').grid(row=2,column=1)
    first=ttk.Entry()
    first.grid(row=2,column=2)
    #no.bind("<Return>",first.set_focus)

    

    last_label=ttk.Label(text='last element').grid(row=3,column=1)
    last=ttk.Entry()
    last.grid(row=3,column=2)
    
    gen=ttk.Button(text="Generate",command=generate)
    gen.grid(row=5,column=1)
    

b1=gui.Radiobutton(text="Enter manually",indicator=0,command=run_manual,variable=v,value=1).grid(row=0,column=1)
b2=gui.Radiobutton(text="Generate Random",indicator=0,command=run_random,variable=v,value=2).grid(row=0,column=2)



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
        a[i-1].bind('<Return>',lambda event:on_change())
        root.bind('<KeyRelease-Return>',lambda event:arry_entry(i))
 




bubble=ttk.Button(text="Bubble-Sort",command=lambda:s.bubble_sort(arr))
bubble.grid(row=6,column=1)

s=sort()
gui.mainloop()