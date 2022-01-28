from tkinter import *
root = Tk()
root.title("Naisheel's file")
root.iconbitmap('C:\\Users\\Hello\\Downloads\\icon.ico')
root.geometry("500x500")

def click(event):
    mylabel=Label(root,text="You clicked a button!")
    mylabel.pack()

mybutton=Button(root,text="Smash here!",command=click)
mybutton.bind("<Key>",click)
mybutton.pack(pady=20)



root.mainloop()