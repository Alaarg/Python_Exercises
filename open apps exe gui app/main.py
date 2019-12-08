# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:47:21 2019

@author: Ahmad ALaarg
"""

import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text

import os

root = tk.Tk()
apps = []
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    fileName = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(fileName)
    print(fileName)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def runApp():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="#ffffff")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10,
                     pady=10, fg="#ffffff", bg="#263D42", command=addApp)

openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=10, fg="#ffffff", bg="#263D42", command=runApp)

runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ",")
