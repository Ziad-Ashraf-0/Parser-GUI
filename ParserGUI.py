import os
dirpath = os.getcwd()
os.environ["PATH"] += os.pathsep + dirpath + os.pathsep + 'graphviz-2.38\\release\\bin'
from tkinter import *
from tkinter import Entry
from tkinter.filedialog import askopenfilename
import tkinter as tk
import grammar as gr
import scanner as src
win = tk.Tk()
var = IntVar()
def readfromfile(INPUTFILE):
    inFile = open(INPUTFILE, 'r') # read from file
    lines = inFile.readlines()
    inFile.close()
    return lines
def main(lines):
    gr.outputs = src.scanner(lines)
    gr.program()
    gr.generate_tree()
win.title("Parser Project")
win.configure(background='#856ff8')
win.geometry("700x600")
win.resizable(False,False)

#----------------------------
#labels in the middle
#----------------------------

label1 = tk.Label(win, text="No option is selected!!",bg="#856ff8", fg="white")
label1.pack()
label2 = tk.Label(win, text="Status: (waiting for inputs)", bg="#856ff8", fg="white")
label2.pack()
label3 = tk.Label(win, text="", bg="#856ff8", fg="white")
label3.pack()

#----------------------------
#TINY label in the LEFT
#----------------------------

Tiny = tk.Label(win , text= "TINY language Parse", width= 17, height= 2, fg= "black")
Tiny.pack()
Tiny.place(bordermode=INSIDE, x=1,y = 10)

#----------------------------
#label above RUN button
#----------------------------

L1 = tk.Label(win , text= "Click Run to parse:", bg="#856ff8", fg="black")
L1.pack()
L1.place(bordermode=INSIDE, x=585, y=505)
#----------------------------
#label above RADIO BUTTON
#----------------------------

L2 = tk.Label(win , text= "Choose your entry method: (Directory/Code)", bg="#856ff8", fg="white")
L2.pack()
L2.place(bordermode=INSIDE, x=10, y=65)

#----------------------------
#Entry of Directory
#----------------------------

E1 = Entry(win, width = 70)
E1.pack()
E1.place(bordermode=OUTSIDE, x=100, y=145)

#----------------------------
#Entry of Code
#----------------------------

E2 = Text(win, width = 70, height = 22)
E2.pack()
E2.place(x= 10, y= 210)

#----------------------------
#label above Directory Entry
#----------------------------

Dir = tk.Label(win , text= "Enter Directory:", bg="#856ff8", fg="white")
Dir.pack()
Dir.place(bordermode=INSIDE, x=10, y=145)

#----------------------------
#label above Code Entry
#----------------------------

Code = tk.Label(win , text= "Enter Code:", bg="#856ff8", fg="white")
Code.pack()
Code.place(bordermode=INSIDE, x=10, y=180)

#----------------------------
#Functions:
#----------------------------

def sel():
   selection = "You selected the option " + str(var.get())
   label1.config(text = selection)
   x = var.get()
   if x == 1:
       label3.config(text="Directory")
       E2.config(state='disabled')
       E1.config(state='normal')
       E2.delete(0, END)
   elif x ==2:
       label3.config(text="Code")
       E1.config(state='disabled')
       E2.config(state='normal')
       E2.delete('1.0', END)
       E1.delete(0, END)

def main_RUN():
    x = var.get()
    if(x==1):
        if(len(Entry.get(E1))):
            label2.config(text="Status: Code is Running...")
            lines = readfromfile(Entry.get(E1))
            main(lines)
        else:
            label2.config(text="Status: Error, please enter a directory at first!")
    elif(x==2):
        if(len(E2.get(1.0, END)) > 1):
            label2.config(text="Status: Code is Running...")
            lines = E2.get(1.0, END)
            lines = lines.split()
            main(lines)
        else:
            label2.config(text="Status: Error, please enter code at first!")
    else:
        label2.config(text="Status: Error, please select an entry method!")
def OpenFileGui():
    filename = askopenfilename()
    if(len(Entry.get(E1))):
        E1.delete(0,END)
    E1.insert(END,filename)
def show():
    if(len(Entry.get(E1))):
        lines = readfromfile(Entry.get(E1))
        E2.config(state='normal')
        E2.delete('1.0', END)
        lines = "".join(lines)
        E2.insert(END,lines)
    else:
        label2.config(text="Status: Error, please select a directory at first!")
#----------------------------
#Buttons:
#----------------------------

R1 = Radiobutton(win, text = "Directory", selectcolor= "black", highlightcolor = "black", activebackground="#856ff8", bg="#856ff8", fg="white", variable = var, value = 1, command = sel)
R1.pack()
R1.place(bordermode=OUTSIDE, x=20, y=90)

R2 = Radiobutton(win, text = "Code", selectcolor= "black", highlightcolor = "black",activebackground="#856ff8", bg="#856ff8", fg="white", variable = var, value = 2, command = sel)
R2.pack()
R2.place(bordermode=OUTSIDE, x=20, y=110)
Run = tk.Button(win, text = "Run", command = main_RUN,  width = 10,activebackground= "black", activeforeground = "green")
Run.pack()
Run.place(x=595, y=540)
OpenFile = tk.Button(win, text = "Open File", command = OpenFileGui,  width = 10,activebackground= "black", activeforeground = "green")
OpenFile.pack()
OpenFile.place(x=595, y=144)
SHOW = tk.Button(win, text = "Show", command = show, width = 10,activebackground= "black", activeforeground = "green")
SHOW.pack()
SHOW.place(x=595, y=210)

win.mainloop()

