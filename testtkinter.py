import tkinter as tk

root=tk.Tk()
root.geometry('300x400')
testbut=tk.Menubutton(root)
l=tk.Label(root,text=print(testbut.__dict__))
l.pack()




tk.mainloop