from tkinter import *
root=Tk()
def rightclick(event):
    print("right clicked")
def leftclick(event):
    print("left clicked")
def middleclick(event):
    print("middle click")
frame=Frame(root,width=300,height=300)
frame.bind("<Button-1>",rightclick)
frame.bind("<Button-2>",leftclick)
frame.bind("<Button-3>",middleclick)
frame.pack()
root.mainloop()
