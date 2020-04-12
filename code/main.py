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
en=1



v=None
root= gui.Tk()
root.geometry("800x1000")
root.resizable(width=False,height=True)

frame=ttk.Frame(root)
frame.configure(width=400,height=400)
BasicLooks=ttk.Style()
BasicLooks.theme_use('alt')
frame.grid(row=1)

#custom-rizing the looks
look_buttons=ttk.Style()
look_buttons.configure('num.TButton',relief='flat',font=('callbri',13,'bold'),bordercolor='black',ipading=0,foreground='black',background='#e6ffff', borderwidth=1, focusthickness=1, focuscolor='none')
look_buttons.map('num.TButton',foreground=[('pressed', 'black'), ('active', 'black')],
    background=[('pressed', '!disabled', '#00ffff'), ('active', '#80ffff')])
look_text1=ttk.Style()
look_text1.configure('text1.TRadiobutton',relief='flat',font=('callbri',20,'bold'),bordercolor='black',ipading=20,foreground='black',background='#e6ffff', borderwidth=1, focusthickness=1, focuscolor='none')
look_text2=ttk.Style()
look_text2.configure('text2.TLabel',relief='flat',font=('callbri',15,'bold'),bordercolor='black',ipading=20,padding=20,foreground='black',background='grey', borderwidth=1, focusthickness=1, focuscolor='none')
look_box=ttk.Style()
look_box.configure('box.TEntry',width=10)



def run_manual():
    frame.update()
    global en,arr
    if en==0:
        arr=[]
        en=1

    text=ttk.Label(frame,text='Enter elments',style='text2.TLabel')
    text.grid(row=1,column=1)
    arry_entry(i)
    
    confirm=ttk.Button(frame,text="Proceed",style='num.TButton',command=last_entry)
    confirm.grid(row=10+d+j,column=1)


def run_random():
    global en,arr
    if en==0:
        arr=[]

    en=0


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
              
            r[i]=ttk.Label(frame,text=arr[i]).grid(row=3+j,column=pos)
        butt()
        
        
             
    no_label=ttk.Label(frame,text='No of elements',style='text2.TLabel').grid(row=1,column=1)
    no=ttk.Entry(justify='center',width=7,style='box.TEntry',font = ('courier', 15, 'bold'))
    no.focus()
    no.grid(row=1,column=2)
    
    first_label=ttk.Label(frame,text=' First element  ',style='text2.TLabel').grid(row=2,column=1)
    first=ttk.Entry(justify='center',width=7,style='box.TEntry',font = ('courier', 15, 'bold'))
    first.grid(row=2,column=2)
    #no.bind("<Return>",first.set_focus)

    

    last_label=ttk.Label(frame,text='  Last element  ',style='text2.TLabel').grid(row=3,column=1)
    last=ttk.Entry(justify='center',width=7,style='box.TEntry',font = ('courier', 15, 'bold'))
    last.grid(row=3,column=2)
    
    gen=ttk.Button(frame,text="Generate",style='num.TButton',command=generate)
    gen.grid(row=10+j+d,column=1)
    


b1=ttk.Radiobutton(text="Enter manually",style='text1.TRadiobutton',command=run_manual,variable=v,value=1).grid(row=0,column=0,sticky=gui.N+gui.W)
b2=ttk.Radiobutton(text="Generate Random",style='text1.TRadiobutton',command=run_random,variable=v,value=2).grid(row=0,column=1,sticky=gui.N+gui.W)


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
        a[i]=ttk.Entry(frame,style='box.TEntry',justify='center',width=5,font = ('courier', 15, 'bold'))
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
    bubble=ttk.Button(text="Bubble-Sort",style='num.TButton',command=lambda:s.bubble_sort())
    bubble.grid(row=11+d+j,column=1)

    merge=ttk.Button(text="Merge-Sort",style='num.TButton',command=lambda:s.merge_sort(arr))
    merge.grid(row=11+d+j,column=2)

    selection=ttk.Button(text="selection-Sort",style='num.TButton',command=lambda:s.selection())
    selection.grid(row=11+d+j,column=3)

s=sort(arr)
gui.mainloop()