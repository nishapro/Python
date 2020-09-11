from tkinter import *
root=Tk()
label1=Label(root,text="one",bg="red")
label2=Label(root,text="two",bg="green")
label3=Label(root,text="three",bg="blue")
label1.pack()
label2.pack(fill=X) ##without side the Y direction will not work
label3.pack(side=LEFT,fill=Y)
root.mainloop()
