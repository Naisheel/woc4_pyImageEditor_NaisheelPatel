from tkinter import *
root = Tk()
root.title("Naisheel's file")
root.iconbitmap('C:\\Users\\Hello\\Downloads\\icon.ico')
root.geometry("500x500")
class first_class:
    def clicker(self):
        print("Hey, you clicked a button")
    def __init__(self, master):
        myFrame=Frame(master)
        myFrame.pack()

        self.myButton= Button(master,text="Smash here!",command=clicker)
        self.myButton.pack()
 
e=first_class(root)




root.mainloop()