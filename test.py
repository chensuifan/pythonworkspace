import tkinter as tk
from typing import Text, TextIO

#整體外寬
root=tk.Tk()
root.title('我的第一個軟件窗口')
root.geometry('980x640')
#

def checkmode():
    if var.get() == 'tcp':
        label.config()
    else:
        label2.configure(text='serial')
def connectd():
    pass
def disconnectd():
    pass
def tcpcon():
    pass
def serial():
    pass

label=tk.Label(root,bd=2,relief='ridge',width=65,height=20).place(x=250,y=45,anchor='nw')
label2=tk.Label(root,bd=2,relief='ridge',width=65,height=10,text='').place(x=250,y=450)
var=tk.StringVar()
farme=tk.Frame(       root,     relief='ridge',     bd=2,           width=200, height=230)                                                  .place(x=5,y=45)
botom1=tk.Button(     root,     text='連接設備',     command=connectd)                                                                  .place(x=12,y=230)
botom2=tk.Button(     root,     text='斷開設備',     command=disconnectd)                                                               .place(x=120,y=230)
radio1=tk.Radiobutton(root,     text='tcp連接',      relief='raise',    bd=2,     variable=var, value='tcp',    command=checkmode)    .place(x=12,y=50)
radio2=tk.Radiobutton(root,     text='serial連接',   relief='raise',    bd=2,     variable=var, value='serial', command=checkmode) .place(x=100,y=50)

    

tk.mainloop()