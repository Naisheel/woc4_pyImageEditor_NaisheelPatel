from tkinter import *
root = Tk()
root.title("Naisheel's file")
root.iconbitmap('C:\\Users\\Hello\\Downloads\\icon.ico')

class first_class:

    def __init__(self, master):
        myFrame=Frame(master)
        myFrame.pack()

        self.myButton=Button(master,text="Smash here!",command=self.clicking)
        self.myButton.pack()
    def clicking(self):
        print("You cliked a button")
e=first_class(root)


root.mainloop()