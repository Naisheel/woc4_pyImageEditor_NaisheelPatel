from tkinter import *
from PIL import ImageTk,Image

root= Tk()
root.title("Naisheel's file")
root.iconbitmap('C:\\Users\\Hello\\Downloads\\icon.ico')

img = ImageTk.PhotoImage(Image.open("C:\\Users\\Hello\\Pictures\\flowchart1.png"))
myLabel = Label(image=img)
myLabel.pack()

button_quit= Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()