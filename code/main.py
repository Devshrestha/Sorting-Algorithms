import tkinter as gui
from tkinter import ttk
import random
from sorting import sort

a=[]
b=[]
arr=[]
i=0
j=1
d=1
en=True


root= gui.Tk()
frame=ttk.Frame(root).grid()
v=None



def run_manual():
    text=ttk.Label(text='Enter elments')
    text.grid(row=1,column=1)
    arry_entry(i)
    confirm=ttk.Button(text="Proceed",command=last_entry)
    confirm.grid(row=10+d+j,column=1)


def run_random():
    


    def generate():
        r=[]
        inp=[]
        global j
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
            pos=i+1
            if pos/(j*10)>1:
                j+=1
            pos=pos-((j-1)*10)
              
            r[i]=ttk.Label(text=arr[i]).grid(row=3+j,column=pos)
            butt()
        
        
             
    no_label=ttk.Label(text='no of elements').grid(row=1,column=1)
    no=ttk.Entry()
    no.focus()
    no.grid(row=1,column=2)
    
    first_label=ttk.Label(text='First element').grid(row=2,column=1)
    first=ttk.Entry()
    first.grid(row=2,column=2)
    #no.bind("<Return>",first.set_focus)

    

    last_label=ttk.Label(text='last element').grid(row=3,column=1)
    last=ttk.Entry()
    last.grid(row=3,column=2)
    
    gen=ttk.Button(text="Generate",command=generate)
    gen.grid(row=10+j+d,column=1)
    

b1=gui.Radiobutton(text="Enter manually",indicator=0,command=run_manual,variable=v,value=1).grid(row=0,column=1)
b2=gui.Radiobutton(text="Generate Random",indicator=0,command=run_random,variable=v,value=2).grid(row=0,column=2)



def last_entry():
    butt()


def arry_entry(i):
    global d
    
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
        #for printing only ten boxes in a row
        pos=i+1
        if (pos/(d*10))>1:
            d+=1
        pos=pos-((d-1)*10)
        a[i].grid(row=1+d,column=pos)
        a[i].focus()
        i+=1
        a[i-1].bind('<Return>',lambda event:on_change())
        root.bind('<KeyRelease-Return>',lambda event:arry_entry(i))
 



def butt():
    bubble=ttk.Button(text="Bubble-Sort",command=lambda:s.bubble_sort(arr))
    bubble.grid(row=11+d+j,column=1)

s=sort()
gui.mainloop()