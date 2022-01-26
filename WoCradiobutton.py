from ast import Lambda
from msilib.schema import RadioButton
from tkinter import *

root = Tk()
r=IntVar()
r.set("2")

dinner = [
    ("Pizza","La pinoz"),
    ("Burger","McD"),
    ("full course","idk")
]

food=StringVar()
food.set("Pizza")
for type,place in dinner:
    Radiobutton(root, text=type,variable=food,value=place).pack(anchor=W)

def clicked(value):
    myLabel= Label(root,text=value)
    myLabel.pack()


#Radiobutton(root,text="Option 1", variable=r,value=1,command=lambda: clicked(r.get())).pack()
#Radiobutton(root,text="Option 2", variable=r,value=2,command=lambda: clicked(r.get())).pack()
myButton = Button(root, text="Smash here",command=lambda:clicked(food.get())).pack()



root.mainloop()