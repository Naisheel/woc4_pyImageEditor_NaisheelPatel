from tkinter import *
from tkinter import messagebox

root= Tk()

def popup():
    response=messagebox.askyesno("This is my popup","Hey there")
    
    if response==1:
        Label(root,text="Yes!!! was clicked").pack()
    else:
        Label(root,text="No was clicked").pack()


Button(root,text="Popup",command=popup).pack()








root.mainloop()