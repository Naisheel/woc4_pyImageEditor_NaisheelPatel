from tkinter import *
root = Tk()
# Creating a Label Widget
myLabel1 = Label(root, text='How are you!?')
myLabel2 = Label(root, text='Naisheel Patel is here')
# Shoving it onto the screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=5)
root.mainloop()