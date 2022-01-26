from tkinter import *
root = Tk()
def myClick():
    myLabel=Label(root,text="my label")
    myLabel.pack()
myButton = Button(root, text="Smash here!",command=myClick,fg="brown",bg="green")
myButton.pack()
root.mainloop()