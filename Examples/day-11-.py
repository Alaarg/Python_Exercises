# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:40:13 2019

@author: Ahmad ALaarg
"""
"""
from tkinter import *
import tkinter as  tk

root = Tk(className= 'My First GUI')
root.geometry(f"500x500+50+50")

#scree_width = root.winfo_screenmmwidth()
#screen_height = root.winfo_screenheight()
#print(scree_width)
#print(screen_height)


label = tk.Label(root, text="Hello world", font=("times", 50,"bold"), padx=10, pady=10)
label.pack()


btn= Button(root, text = 'Click Here !')
btn.pack()

name = Label(root, text="name").place(x =30)
email= Label(root, text='Exail').place(x=30)

inp_name = Entry(root).place(x=80)
inp_email = Entry(root).place(x=80)
"""
"""
def pressed():
    print('Hello world')

print_btn = Button(root, text = 'press Me to print hello world in consol  ', command = pressed)
print_btn.pack(pady=10)

def Pressed():
    dialog_title="please answer"
    dialog_text="Do you like to travel?"
    answer=messagebox.askquestion(dialog_title,dialog_text)
    if answer=='yes':
        print("You Click Yes")
    else:
        print("You Click No")
alert_btn=Button(root,text="Press Me to open alert",command=Pressed)
alert_btn.pack()


v= StringVar()
e = Entry(root, textvariable=v)
e.pack()
v.set('orange Academy')

def Print_in_inp():    

    print(v.get())



btn_inp =Button(root, text ="click to print input val in consol" , pady=10 , command=Print_in_inp)
btn_inp.pack()



root.mainloop()
"""
"""
from tkinter import *
root = Tk()
root.title('menu_win')
def notdone():
    messagebox.showinfo('Not implemented', 'Not yet available')
top = Menu(root)
root.config(menu=top)
file = Menu(top,tearoff=0)
file.add_command(label='New...', command=notdone)
file.add_command(label='Open...', command=notdone)
file.add_separator()
file.add_command(label='Quit', command=root.destroy)
top.add_cascade(label='File', menu=file)
edit = Menu(top,tearoff= 0)
edit.add_command(label='Cut', command=notdone)
edit.add_command(label='Paste', command=notdone)
top.add_cascade(label='Edit', menu=edit)
root.mainloop()
"""

"""
from tkinter import *
from tkinter.colorchooser import *
def getColor():
    color = askcolor()
    print (color)
Button(text='Select Color', command=getColor).pack()
mainloop()


"""
"""


from tkinter import *
master = Tk()
w = Canvas(master, width=200, height = 100)
w.pack()
w.create_rectangle(50,20,150,80, fill="#476042")
w.create_rectangle(65,35,135,65, fill="yellow")
w.create_line(0,0,50,20, fill ="#476042", width=3)
w.create_line(0,100,50,80, fill ="#476042", width=3)
w.create_line(150,20,200,0, fill ="#476042", width=3)
w.create_line(150,80,200,100, fill ="#476042", width=3)
mainloop()
"""

"""
import tkinter as Tk
class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.label = tk.Label(self, text ="Hello world", padx=5, pady=5)
        self.label.pack()
if __name__ == "__main__":
    root = Root()
    root.mainloop()
"""

from tkinter import *
import urllib.request
def go():
	text.delete(1.0, END)
	with urllib.request.urlopen(entry.get()) as response:
		received_html = response.read()
	text.insert(1.0, received_html)

browser_window = Tk()
browser_window.title('knowpapa browser')
label = Label(browser_window, text= 'Enter URL:')
entry = Entry(browser_window)
entry.insert(END, "https://knowpapa.com")
button = Button(browser_window, text='Go', command = go)
text = Text(browser_window)
label.pack(side=TOP)
entry.pack(side=TOP)
button.pack(side=TOP)
text.pack(side= TOP)
browser_window.mainloop()















