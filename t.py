import tkinter
from tkinter.constants import Y
'''tcp連接按鈕的輸入框還沒有調好'''




# 窗口初始化，大小
tk=tkinter.Tk()
tk.title('網絡串口連接工具')
tk.geometry('1000x700')
# 創建框架
comout=tkinter.Frame(tk,bd=2,relief='ridge',width=680,height=360).place(x=300,y=30)
connect=tkinter.Frame(tk,bd=2,relief='ridge',width=250,height=360).place(x=30,y=30)
scdconnect=tkinter.Frame(tk,bd=2,relief='ridge',width=250,height=360).place(x=30,y=30)
osframe=tkinter.Frame(tk,bd=2,relief='ridge',width=950,height=270).place(x=30,y=400)


# 獲取連接方式,ip地址，端口號，串口號，波特率A
whatcnt=tkinter.IntVar()
ip=tkinter.StringVar()
ip.set('192.168.0.1')
port=tkinter.IntVar()
port.set('80')
com=tkinter.StringVar()
com.set('com1')
bote=tkinter.IntVar()
bote.set('115200')

# 顯示網絡連接tcp ip 端口號
def showcnt():
    if whatcnt.get() == 1:
        scdconnect.quit()
        # 顯示tcp窗口
        tkinter.Label(connect,text='IP地址:').place(x=50,y=120)
        tkinter.Label(connect,text='端口號:').place(x=50,y=220)
        tkinter.Entry(connect,textvariable=ip,width=12).place(x=150,y=120)
        tkinter.Entry(connect,textvariable=port,width=12).place(x=150,y=220)
        
    elif whatcnt.get() == 2:
        tkinter.Label(scdconnect,text='串口號:').place(x=50,y=120)
        tkinter.Label(scdconnect,text='波特率:').place(x=50,y=220)
    else:
        print('錯誤')
def connectbut():
    pass
def disconnect():
    pass
# 創建tcp串口選擇按鈕
tkinter.Radiobutton(tk,text='網絡連接',variable=whatcnt,value=1,command=showcnt,width=10,height=1).place(x=38,y=40)
serialbut=tkinter.Radiobutton(tk,text='串口連接',variable=whatcnt,value=2,command=showcnt,width=10,height=1).place(x=140,y=40)
# 創建連接，斷開按鈕
tkinter.Button(tk,text='連接設備',command=connectbut,width=10,height=1).place(x=50,y=320)
tkinter.Button(tk,text='斷開設備',command=disconnect,width=10,height=1).place(x=160,y=320)







tk.mainloop()


