from tkinter import *
root = Tk()
root.title("Naisheel's file")
root.iconbitmap('C:\\Users\\Hello\\Downloads\\icon.ico')
root.geometry("2500x2500")

w= 2500
h= 2500
x=w//2
y=h//2

myCanvas= Canvas(root,width=w,height=h,bg="white")
myCanvas.pack(pady=20)
#adding image to canvas
img= PhotoImage(file="C:\\Users\\Hello\\Downloads\\image.png")
myimage=myCanvas.create_image(0,0,anchor=NW,image=img)
def left(event):
    x=-10
    y=0
    myCanvas.move(myimage,x,y)
def right(event):
    x=10
    y=0
    myCanvas.move(myimage,x,y)
def up(event):
    x=0
    y=-10
    myCanvas.move(myimage,x,y)
def down(event):
    x=0
    y=10
    myCanvas.move(myimage,x,y)

root.bind("<Left>",left)
root.bind("<Right>",right)
root.bind("<Up>",up)
root.bind("<Down>",down)

root.mainloop()