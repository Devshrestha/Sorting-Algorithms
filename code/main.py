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
enter=0
prev=[]
value=0

frame_width=700
frame_height=700
v=None
root= gui.Tk()
root.geometry("700x750")
root.configure(background="#d9d9d9")
root.resizable(width=False,height=True)

frame=ttk.Frame(root)
frame.configure(width=frame_width,height=frame_height/3)
frame.grid(row=1,columnspan=2)
frame2=ttk.Frame(root)
frame2.configure(width=frame_width,height=frame_height/3)
frame2.grid(row=2,columnspan=2)
frame3=ttk.Frame(root)
frame3.configure(width=frame_width,height=frame_height/3)
frame3.grid(row=3,columnspan=2)
BasicLooks=ttk.Style()
BasicLooks.theme_use('alt')


#custom-rizing the looks
look_buttons=ttk.Style()
look_buttons.configure('num.TButton',relief='flat',font=('callbri',13,'bold'),bordercolor='black',ipading=0,foreground='black',background='#e6ffff', borderwidth=1, focusthickness=1, focuscolor='none')
look_buttons.map('num.TButton',foreground=[('pressed', 'black'), ('active', 'black')],
    background=[('pressed', '!disabled', '#00ffff'), ('active', '#80ffff')])
look_sort_butt=ttk.Style()
look_sort_butt.configure('sort.TButton',relief='flat',font=('callbri',13,'bold'),bordercolor='black',padding=10,ipadding=20,foreground='black',background='#e6ffff', borderwidth=1, focusthickness=1, focuscolor='none')
look_sort_butt.map('sort.TButton',foreground=[('pressed', 'black'), ('active', 'black')],
    background=[('pressed', '!disabled', '#00ffff'), ('active', '#0099ff')])
look_text1=ttk.Style()
look_text1.configure('text1.TRadiobutton',relief='flat',font=('callbri',20,'bold'),bordercolor='black',ipading=20,foreground='black',background='#e6ffff', borderwidth=1, focusthickness=1, focuscolor='none')
look_text2=ttk.Style()
look_text2.configure('text2.TLabel',relief='flat',font=('callbri',15,'bold'),bordercolor='black',ipading=20,padding=20,foreground='black', borderwidth=1, focusthickness=1, focuscolor='none')
look_box=ttk.Style()
look_box.configure('box.TEntry',width=8)
look_gen=ttk.Style()
look_gen.configure('text3.TLabel',relief='flat',font=('callbri',10,'bold'),bordercolor='black',ipading=20,padding=20,foreground='black', borderwidth=1, focusthickness=1, focuscolor='none')



def run_manual():
    global enter,frame,frame2,frame3
    if enter==1:
        frame.destroy()
        frame2.destroy()
        frame3.destroy()
        frame=ttk.Frame(root)
        frame.configure(width=frame_width,height=frame_height/3)
        frame.grid(row=1,columnspan=2)
        frame2=ttk.Frame(root)
        frame2.configure(width=frame_width,height=frame_height/3)
        frame2.grid(row=2,columnspan=2)
        frame3=ttk.Frame(root)
        frame3.configure(width=frame_width,height=frame_height/3)
        frame3.grid(row=3,columnspan=2)
    enter=1
    #frame.update()
    global en,arr
    if en==0:
        arr=[]
        en=1

    text=ttk.Label(frame,text='Enter elments',style='text2.TLabel')
    text.grid(row=0,column=1,sticky=gui.N+gui.W)
    arry_entry(i)
    
    confirm=ttk.Button(frame2,text="Next",style='num.TButton',command=last_entry)
    confirm.configure(width=7)
    confirm.grid(row=10+d+j,column=1)


def run_random():
    global en,arr,enter,frame,frame2,frame3,prev
    if enter==1:
        frame.destroy()
        frame2.destroy()
        frame3.destroy()
        frame=ttk.Frame(root)
        frame.configure(width=frame_width,height=frame_height/3)
        frame.grid(row=1,columnspan=2)
        frame2=ttk.Frame(root)
        frame2.configure(width=frame_width,height=frame_height/3)
        frame2.grid(row=2,columnspan=2)
        frame3=ttk.Frame(root)
        frame3.configure(width=frame_width,height=frame_height/3)
        frame3.grid(row=3,columnspan=2)
    enter=1
    if en==0:
        arr=[]

    en=0


    def generate():
        r=[]
        inp=[]
        global j,prev
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
              
            r[i]=ttk.Label(frame2,style='text3.TLabel',text=arr[i]).grid(row=0+j,column=pos)
        prev=arr
        butt()
        
        

    def change_focus(x):
        x.focus()


    last_label=ttk.Label(frame,text='  Last element  ',style='text2.TLabel')
    last_label.grid(row=2,column=1)
    last=ttk.Entry(frame,justify='center',width=7,style='box.TEntry',font = ('courier', 15, 'bold'))
    last.grid(row=2,column=2)

    first_label=ttk.Label(frame,text=' First element  ',style='text2.TLabel')
    first_label.grid(row=1,column=1)
    first=ttk.Entry(frame,justify='center',width=7,style='box.TEntry',font = ('courier', 15, 'bold'))
    first.grid(row=1,column=2)
    first.bind("<KeyRelease-Return>",lambda event:change_focus(last))
    

    no_label=ttk.Label(frame,text='No of elements',style='text2.TLabel')
    no_label.grid(row=0,column=1)
    no=ttk.Entry(frame,justify='center',width=7,style='box.TEntry',font = ('courier', 15, 'bold'))
    no.focus()
    no.bind("<KeyRelease-Return>",lambda event:change_focus(first))
    no.grid(row=0,column=2)
    
    

    

    
    gen=ttk.Button(frame,text="Generate",style='num.TButton',command=generate)
    gen.grid(row=10+j+d,column=1)
    


b1=ttk.Radiobutton(text="Enter manually",style='text1.TRadiobutton',command=run_manual,variable=v,value=1).grid(row=0,column=0,sticky=gui.N+gui.W)
b2=ttk.Radiobutton(text="Generate Random",style='text1.TRadiobutton',command=run_random,variable=v,value=2).grid(row=0,column=1,sticky=gui.N+gui.W)


def last_entry():
    global prev,arr
    prev=arr
    butt()
    


def arry_entry(i):
    global d
    
    def on_change():
        
        try:
            #if  type(a[i-1].get()) == int or  type(a[i-1].get())==float:  
            b.append(float(a[i-1].get()))
            
        except ValueError:
            print('error')
        if float(b[i-1])==int(b[i-1]):
            arr.append(int(b[i-1]))
            
        elif type(b[i-1])==float:
            arr.append(float(b[i-1]))
        

                
    
    if en:
        a.append(None)
        a[i]=ttk.Entry(frame2,style='box.TEntry',justify='center',width=5,font = ('courier', 15, 'bold'))
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

def output(value):
    i=1
    j=1
    r=[]
    global frame2,prev,arr
    frame2.destroy()
    frame2=ttk.Frame(root)
    frame2.configure(width=frame_width,height=frame_height/3)
    frame2.grid(row=2,columnspan=2)

    output_text=ttk.Label(frame2,text="SORTED LIST:",style='text2.TLabel',foreground='red')
    output_text.grid(row=0,column=0,columnspan=8)

    for i in range(len(value)): 
        r.append(None)     
        pos=i+1
        if pos/(j*10)>1:
            j+=1
        pos=pos-((j-1)*10)
            
        r[i]=ttk.Label(frame2,style='text3.TLabel',text=value[i]).grid(row=0+j,column=pos)
    
    arr=prev
    print(prev)
    butt()

def buttonpress(function, *args):
    global value
    value = function(*args)
    if function == s.merge_sort:
        value=arr 
    output(value)

def butt():
    
    bubble=ttk.Button(frame3,text="Bubble-Sort",style='sort.TButton',command=lambda:buttonpress(s.bubble_sort))
    bubble.grid(row=1,column=1,padx=10,pady=10)

    merge=ttk.Button(frame3,text="Merge-Sort",style='sort.TButton',command=lambda:buttonpress(s.merge_sort,arr))
    merge.grid(row=1,column=2,padx=10,pady=10)

    selection=ttk.Button(frame3,text="Selection-Sort",style='sort.TButton',command=lambda:buttonpress(s.selection))
    selection.grid(row=1,column=3,padx=10,pady=10)

    insertion=ttk.Button(frame3,text="Insertion-Sort",style='sort.TButton',command=lambda:buttonpress(s.insertion))
    insertion.grid(row=1,column=4,padx=10,pady=10)

s=sort(arr)
gui.mainloop()