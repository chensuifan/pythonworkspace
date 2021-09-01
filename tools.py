import tkinter
from tkinter.constants import BOTTOM, END
import tkinter.ttk
from typing import Text
import serial
import threading
import time
import mysocketclient



'''
    調試好了：
        tcp調試好了用tk.place.froget()
        串口連接調試好了，引入一個全局變量控制綫程的開關
    未能調試好的：
        調整tcpsocket 連接
        tcp鏈接不上，剛剛修改接收函數
        
        
'''




# 窗口初始化，大小
tk=tkinter.Tk()
tk.title('網絡串口連接工具')
tk.geometry('1000x700')
# 創建框架
comout=tkinter.Frame(tk,bd=2,relief='ridge',width=680,height=360).place(x=300,y=30)     #輸出窗口
showconnect=tkinter.Frame(tk,bd=2,relief='ridge',width=250,height=360).place(x=30,y=30) #連接窗口
connect=tkinter.Frame(tk,bd=2,relief='ridge',width=250,height=360)                      #連接窗口
scdconnect=tkinter.Frame(tk,bd=2,relief='ridge',width=250,height=360)                   #連接窗口
osframe=tkinter.Frame(tk,bd=2,relief='ridge',width=950,height=270).place(x=30,y=400)    #輸入窗口

# 創建顯示窗口

text1= tkinter.Text(comout,width=61,height=21)
text1.place(x=305,y=35)
text1.tag_config("tag_1", foreground="red")# 創建窗口時間顯示的字體大小和顔色
text1.tag_config("tag_2", foreground="blue")# 創建窗口數據顯示的字體大小和顔色
text1.insert(END,'歡迎光臨'+'\n')

# 創建輸入窗口

text2= tkinter.Text(comout,width=90,height=16)
text2.place(x=35,y=405)
text2.tag_config("tag_2", foreground="blue")# 創建窗口數據顯示的字體大小和顔色
text2.insert(END,'在這裏輸入數據'+'\n')

# 獲取連接方式,ip地址，端口號，串口號，波特率A
whatcnt=tkinter.IntVar()
ip=tkinter.StringVar()
ip.set('192.168.0.1')
port=tkinter.IntVar()
com=tkinter.StringVar()
bote=tkinter.IntVar()
bote.set('115200')
closecon=tkinter.StringVar()
tcp_mode=tkinter.StringVar()
bool = True

# 顯示網絡連接tcp ip 端口號
def showcnt():
    if whatcnt.get() == 1:
        scdconnect.place_forget()
        connect.place(x=30,y=30)
        # 顯示tcp窗口
        tkinter.Label(connect,text='協議類型:').place(x=20,y=70)
        tcpcombobox=tkinter.ttk.Combobox(connect,textvariable=tcp_mode,width=10,values=('tcp server','tcp client','udp')).place(x=120,y=70)
        tkinter.Label(connect,text='IP地址:').place(x=20,y=120)
        tkinter.Label(connect,text='端口號:').place(x=20,y=220)
        tkinter.Entry(connect,textvariable=ip,width=12).place(x=120,y=120)
        tkinter.Entry(connect,textvariable=port,width=12).place(x=120,y=220)        
    elif whatcnt.get() == 2:
        connect.pack_forget()
        scdconnect.place(x=30,y=30)
        tkinter.Label(scdconnect,text='串口號:').place(x=20,y=120)
        bote=tkinter.Label(scdconnect,text='波特率:').place(x=20,y=220)
        combobox=tkinter.ttk.Combobox(scdconnect,textvariable=com,values=('com1','com2','com3','com4','com5'),width=10)
        combobox.current(0)
        combobox.place(x=120,y=120)
        botebobox=tkinter.ttk.Combobox(scdconnect,textvariable=bote,values=(115200,57600,38400,19200,9600),width=10)
        botebobox.current(0)
        botebobox.place(x=120,y=220)
    else :
        print('打印錯誤')


#打開串口，調用串口
ser = serial.Serial()#初始化串口數據
ser.baudrate = bote.get()   #設置波特率
ser.bytesize = 8
ser.parity = serial.PARITY_NONE
ser.stopbits = 1
over_time = 30


# 讀取串口數據
def serialcon():
    global bool
    def test():
        while bool:
            end_time=time.time()
            if end_time - starttime < over_time:
                ch = ser.readline() # 讀取一行數據   # 如果需要處理發來的數據請在這裏添加函數處理ch
                text1.insert(END,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'\n',"tag_1")
                text1.insert(END,ch,"tag_2") 
                text1.see(tkinter.END)
                text1.update()
    if ser.is_open== False:
        try:
            ser.port = com.get() #獲取串口號
            ser.open() # 开启串口
            starttime=time.time()
            thread=threading.Thread(target=test)
            thread.start()
        except:
            ser.close()

#他開TCP，連接TCP

mytcp=mysocketclient.mytcpclient()
mytcp.open(ip.get(),port.get())




# 關閉串口連接

def serialclose():
    global bool
    try:
        bool= False
        ser.close()
    except:
        print('錯誤')


def open():
    global bool
    if whatcnt.get() ==1:
        tcprecv= mytcp.myrecv()
        mytcp.start()
        text1.insert(END,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'\n',"tag_1")
        text1.insert(END,tcprecv,"tag_2") 
        text1.see(tkinter.END)
        text1.update()
    elif whatcnt.get() ==2:
        bool = True
        serialcon()


def close():
    if whatcnt.get() ==1:
        mytcp.close()
    elif whatcnt.get() ==2:
        serialclose() # 關閉串口
    else:
        pass

# 創建tcp串口選擇按鈕
tcp=tkinter.Radiobutton(tk,text='網絡連接',variable=whatcnt,value=1,command=showcnt,width=10,height=1)
tcp.place(x=38,y=40)
serial2=tkinter.Radiobutton(tk,text='串口連接',variable=whatcnt,value=2,command=showcnt,width=10,height=1)
serial2.place(x=140,y=40)

# 創建連接，斷開按鈕
tkinter.Button(tk,text='連接設備',command=open,width=10,height=1).place(x=50,y=320)
tkinter.Button(tk,text='斷開設備',command=close,width=10,height=1).place(x=160,y=320)

def serialsend():
    if whatcnt.get() ==1:
        pass
    elif whatcnt.get() ==2:
        if ser.is_open== True:
            serialsenddata=text2.get(1.0,END)
            # 如果需要處理發出去的數據請在這裏添加一個函數處理
            ser.write(serialsenddata.encode('GBK'))
        else :
            text1.insert(END,'串口沒有打開，請先打開串口！！！！',"tag_2")
    else:
        text1.insert(END,'連接沒有打開，請先連接設備！！！！',"tag_2")

# 創建發送數據按鈕
senddatabut=tkinter.Button(osframe,text='發送數據',command=serialsend,width=10,height=1)
senddatabut.place(x=758,y=405)












tk.mainloop()


