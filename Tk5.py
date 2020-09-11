from tkinter import *
root=Tk()
def call_me(event):
    print("I'am called")
button=Button(root,text="click me")
button.bind("<Button-1>",call_me)
button.pack()
root.mainloop()
