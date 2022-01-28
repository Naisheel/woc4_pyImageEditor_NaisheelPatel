from tkinter import *
root = Tk()
root.title("Naisheel's file")
root.iconbitmap('C:\\Users\\Hello\\Downloads\\icon.ico')
root.geometry("500x500")

my_canvas= Canvas(root,width=400,height=400,bg="white")
my_canvas.pack(pady=25)

#in rectangle x1,y1,x2,y2 where x1 and y1 are top left coordinates and x2,y2 are bottom right
my_canvas.create_rectangle(50,350,350,50,fill="yellow")

#here same as rectangle, creating it and oval fitting inside
my_canvas.create_oval(50,350,350,50,fill="red")

#here they are start and end points respectively
my_canvas.create_line(0,200,400,200,fill="green")
my_canvas.create_line(200,0,200,400,fill="green")


root.mainloop()