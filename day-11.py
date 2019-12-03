# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:35:44 2019

@author: Ahmad ALaarg
"""

from tkinter import *
import tkinter as  tk
from tkinter import scrolledtext
from tkinter.colorchooser import *
# Q1 -------------------------------------------------------------
"""
root = Tk(className= 'My First GUI')

root.geometry(f"500x500+50+50")

label = tk.Label(root, text="LogIn ", font=("times", 50,"bold"), padx=10, pady=10)
label2 = tk.Label(root, text="Plese Enter User Name And Password ", font=("times", 10,"bold"), padx=10, pady=10)

label.pack()
label2.pack()

name = Label(root, text="name").place(x =30 , y=150)
email= Label(root, text='Exail').place(x=30, y=200)


v1= StringVar()
v2= StringVar()

inp_name = Entry(root, textvariable=v1).place(x=80,  y=150)
inp_email = Entry(root, textvariable=v2).place(x=80, y=200)

v1.set('Enter your Name')
v2.set('Enter your password')

def login_fun():
    get_name = v1.get()
    get_pass = v2.get()
    
    if v1.get() == "ahmad" and v2.get() == "123" :
        print('you log in ')
    else :
            print('user not valid')
     

login =Button(root, text ="Login" , pady=10, padx=50 ,  command=login_fun).place(x=80, y=250)


root.mainloop()
"""

#Q4 ----------------------------------------------
"""
def open_child1():
    dialog_title=""
    dialog_text="This is a message"
    answer=messagebox.showinfo(dialog_title,dialog_text)
def open_child2():
    top=Tk()
    top.title('Child window 2')
    top.geometry('400x250')
    name=Label(top,text="Emy Number").place(x=30,y=50)
    email=Label(top,text="Emy Name").place(x=30,y=90)
    e1=Entry(top).place(x=100,y=50)
    e2=Entry(top).place(x=100,y=90)
    button=Button(top,text="Quit",command=top.destroy).place(x=150,y=150)
    button.pack()
    top.mainloop()
def open_child3():
    win=Tk()
    win.title("Welcome")
    win.geometry('350x200')
    txt=scrolledtext.ScrolledText(win,width=40,height=10)
    txt.grid(column=0,row=0)
    for r in range(20):
        print(' ')
    win.mainloop()
root = Tk()
root.title('Root window')
Button(root, text = 'open child window 1', command = open_child1).grid()
Button(root, text = 'open child window 2', command = open_child2).grid()
Button(root, text = 'open child window 3', command = open_child3).grid()
root.mainloop()

"""
#Q3---------------------------------------------------
"""
root = Tk()
def getcolor():
    color=askcolor()
    root.config(background=color[1])
Button(root,text="select",command=getcolor).pack()
mainloop()
"""












