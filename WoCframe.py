from tkinter import *
root = Tk()
frame = LabelFrame(root,text="This is Naisheel's frame",padx=5,pady=5)
frame.pack(padx=10,pady=10)
b = Button(frame,text="Hey there")
b.pack()

root.mainloop()