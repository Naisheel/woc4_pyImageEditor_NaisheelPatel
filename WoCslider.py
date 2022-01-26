from distutils import command
from tkinter import *
from tkinter import messagebox

root= Tk()

root.geometry("400x400")

def slide():
    myLabel=Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+ "x"+ str(vertical.get()))

vertical= Scale(root, from_=0,to=500)
vertical.pack()
horizontal= Scale(root, from_=0,to=500,orient=HORIZONTAL)
horizontal.pack()
myLabel=Label(root,text=horizontal.get()).pack()

mybutton= Button(root,text="Smash here!",command=slide).pack()


root.mainloop()