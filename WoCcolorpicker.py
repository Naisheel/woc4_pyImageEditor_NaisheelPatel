from tkinter import *
from tkinter import colorchooser
root = Tk()
root.title("Naisheel's file")
root.iconbitmap('C:\\Users\\Hello\\Downloads\\icon.ico')
root.geometry("500x500")

def color():
    mycolor=colorchooser.askcolor()[1]
    mylabel=Label(root,text=mycolor)
    mylabel.pack(pady=10)
    mylabel2=Label(root,text="The picked colour",font=("Helvetica",30),bg=mycolor).pack()

mybutton=Button(root,text="Pick a colour that suits your need",command=color)
mybutton.pack()




root.mainloop()